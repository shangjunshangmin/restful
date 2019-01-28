"""restful_f URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
\Including another URLconf
\    1. Import the include() function: from django.urls import include, path
\       2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
import xadmin
# from django.urls import path,include
from django.conf.urls import url,include
from restful_f.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsList,GoodsTypeList
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from user.views import SmsCodeViewset,UserViewset
# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'goods', GoodsList,base_name='goods')
router.register(r'categorys', GoodsTypeList,base_name='goodstype')
router.register(r'code', SmsCodeViewset,base_name='code')
router.register(r'users', UserViewset, base_name="users")
urlpatterns = [
    url('admin/', xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    # drf自带的认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证模式
    url(r'^login/', obtain_jwt_token),

]



