# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/5 0005 下午 8:40'
import xadmin
from user_operation.models import UserCollect, UserAddress, UserMessage


class UserCollectAdmin(object):
    list_display = ['user', 'goods', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message_type', 'subject', 'file', 'add_time']


class UserAddressAdmin(object):
    list_display = ['user', 'address', 'signer_name', 'signer_mobile', 'add_time']


xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
