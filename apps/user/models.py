from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    username = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='用户名', unique=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月日')
    phone = models.CharField(null=False,blank=False, verbose_name='手机号码', max_length=11)
    gender = models.CharField(max_length=20, choices=(
        ('man', '男'), ('female', '女')), default='female')
    email = models.EmailField(
        verbose_name='邮箱',
        null=False,
        blank=False,
        max_length=30)

    class Meta:
        managed=True
        verbose_name = '用户组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Code(models.Model):
    # 电话验证码
    code = models.CharField(max_length=15, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code



