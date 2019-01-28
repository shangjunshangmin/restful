from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .Serializers import SmsSerializers, UserRegSerializer
from random import choice
from restful_f.settings import api_key
from .models import Code
# from yunpian import YunPian

# Create your views here.
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))
            print(username, '123', user)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializers

    def generate_code(self):
        '''形成4个数字的验证码'''
        sends = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(sends))
            print(random_str)
        return ''.join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["mobile"]
        yun_pian = YunPian(api_key)
        # 生成验证码
        code = self.generate_code()

        sms_status = yun_pian.send_sms(code=code, mobile=phone)

        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = Code(code=code, mobile=phone)
            code_record.save()
            return Response({
                "mobile": phone
            }, status=status.HTTP_201_CREATED)


class UserViewset(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
