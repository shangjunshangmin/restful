from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime
from django.conf import settings
User = get_user_model()
# Create your models here.


class UserCollect(models.Model):
    # 用户收藏
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    goods = models.ForeignKey(
        Goods,
        verbose_name='商品',
        on_delete=models.CASCADE)
    add_time = models.IntegerField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserMessage(models.Model):
    # 用户留言
    message_type = ((1, "留言"),
                    (2, "投诉"),
                    (3, "询问"),
                    (4, "售后"),
                    (5, "求购"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    message_type = models.CharField(
        max_length=20,
        verbose_name='留言类型',
        help_text='留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)',
        choices=message_type,
    )
    subject = models.CharField(max_length=200, verbose_name='主题', default='')
    file = models.FileField(
        upload_to='message/images',
        verbose_name='上传文件',
        help_text='上传文件')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    # 用户收货地址
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_name = models.CharField(
        max_length=100, default="", verbose_name="签收人")
    signer_mobile = models.CharField(
        max_length=11, default="", verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
