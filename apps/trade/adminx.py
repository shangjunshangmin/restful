# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/5 0005 下午 8:40'
from trade.models import ShoppingCart, OrderInfo, OrderDetail
import xadmin


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'num', 'add_time']
    list_filter = ['user']
    model_icon = 'fa fa-shopping-cart'


class OrderInfoAdmin(object):
    list_display = ['user', 'order_num', 'trade_num', 'pay_model', 'pay_status', 'order_message', 'order_money',
                    'pay_time', 'address', 'signer_user', 'signer_phone', 'add_time']

    class OrderDetailAdmin(object):
        model = OrderDetail
        extra = 1
        style = 'tab'

    inlines = [OrderDetailAdmin, ]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
