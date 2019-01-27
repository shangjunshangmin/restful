# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2019/1/23 0023 下午 9:27'
from rest_framework import serializers
from datetime import datetime, timedelta
from restful_f.settings import REGEX_MOBILE
from .models import Code
import re
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class SmsSerializers(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, min_length=11)

    def validate_mobile(self, mobile):

        '''手机号码注册'''
        if User.objects.filter(phone=mobile).count():
            raise serializers.ValidationError('用户已经注册')
        '''是否符合正则表达式'''
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')
        '''验证码发送频率，每分钟发送一次'''
        one_minutes_ago = datetime.now() - timedelta(days=0, minutes=1, seconds=0)
        if Code.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError('距离上次发送未满60s')
        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    '''
    用户注册
    '''
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, allow_blank=False,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码", label='验证码')
    # 验证用户名是否存在
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(label='密码', help_text='请输入密码', required=True, allow_blank=False, write_only=True,
                                     style={'input_type': 'password'}, max_length=8, min_length=8,
                                     error_messages={"max_length": "密码必须为8位数", "min_length": "密码必须为8位数",
                                                     "blank": "请输入验证码", })

    # 验证code
    def validate_code(self, code):
        # 用户注册，已post方式提交注册信息，post的数据都保存在initial_data里面
        # username就是用户注册的手机号，验证码按添加时间倒序排序，为了后面验证过期，错误等
        verify_records = Code.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")

        if verify_records:
            # 最近的一个验证码
            last_record = verify_records[0]
            # 有效期为五分钟。
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            print(five_mintes_ago, last_record.add_time)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("用户名错误")

        # 所有字段。attrs是字段验证合法之后返回的总的dict

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        # 前端没有传mobile值到后端，这里添加进来
        attrs["phone"] = attrs["username"]
        # code是自己添加得，数据库中并没有这个字段，验证完就删除掉
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ('username', 'code', 'phone', 'password')
