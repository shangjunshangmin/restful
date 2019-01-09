from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime

User = get_user_model()

# Create your models here.


class ShoppingCart(models.Model):
    # 购物车
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    goods = models.ForeignKey(
        Goods,
        verbose_name='商品',
        on_delete=models.CASCADE)
    num = models.IntegerField(default=0, verbose_name='购买数量')
    add_time = models.IntegerField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s%d' % (self.user, self.num
                         )


class OrderInfo(models.Model):
    # 订单
    order_status = (("TRADE_SUCCESS", "成功"),
                    ("TRADE_CLOSED", "超时关闭"),
                    ("TRADE_CREATE", "交易创建"),
                    ("TRADE_FINISHED", "交易结束"),
                    ("paying", "待支付"),)
    order_pay = (('qq', 'qq支付'), ('weixin', '微信支付'))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='用户',
        max_length=30,
        on_delete=models.CASCADE)
    order_num = models.CharField(
        verbose_name='订单号',
        max_length=25,
        null=True,
        blank=True,
        unique=True)
    trade_num = models.CharField(
        verbose_name='交易号',
        max_length=25,
        null=True,
        blank=True,
        unique=True)
    pay_model = models.CharField(
        verbose_name='支付方式',
        choices=order_pay,
        max_length=30,
        default='qq')
    pay_status = models.CharField(
        verbose_name='支付状态',
        max_length=80,
        choices=order_status, default='paying')
    order_message = models.CharField(verbose_name='订单留言', max_length=200)
    order_money = models.DecimalField(
        verbose_name='订单金额',
        max_digits=8,
        decimal_places=2)
    pay_time = models.DateField(verbose_name='支付时间', default=datetime.now)
    # 用户信息
    address = models.CharField(verbose_name='收货地址', max_length=150, default='')
    signer_user = models.CharField(
        verbose_name='签收人', max_length=20, default='')
    signer_phone = models .CharField(
        verbose_name='联系电话', max_length=11, default='')
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_num


class OrderDetail(models.Model):
    # 订单详情

    order = models.ForeignKey(
        OrderInfo,
        verbose_name='订单信息',
        on_delete=models.CASCADE)
    goods = models.ForeignKey(
        Goods,
        verbose_name='商品',
        on_delete=models.CASCADE)
    goods_num = models.IntegerField(
        default=0,
        verbose_name='商品数量',
        )
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_num)
