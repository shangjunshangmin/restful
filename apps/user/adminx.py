# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/5 0005 下午 8:40'
from user.models import Code
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '尚军学习后台'
    site_footer = '学习'
    menu_style = 'accordion'


class CodeAdminSetting(object):
    list_display = ['code', 'mobile', 'add_time']
    list_filter = ['code', 'mobile', 'add_time']
    search_fields = ['code', 'mobile', 'add_time']
    refresh_times = [3, 5]
    model_icon = "fa fa-commenting-o"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Code, CodeAdminSetting)
