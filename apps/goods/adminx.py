# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/5 0005 下午 8:40'
import xadmin
from goods.models import *


class GoodTypeAdmin(object):
    # 商品种类
    list_display = ['name', 'category_type', 'parent_type', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    relfield_style = 'fk-ajax'


class BrandAdmin(object):
    # 品牌名称
    list_display = ['category', 'name', 'desc', 'image', 'add_time']
    list_filter = ['add_time', 'name']
    search_fields = ['name']
    relfield_style = 'fk-ajax'


class GoodsAdmin(object):
    list_display = ['type', 'goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'good_nums', 'market_price',
                    'shop_price', 'goods_brief', 'goods_des', 'ship_free', 'goods_front_image', 'is_new', 'is_hot']
    search_fields = ['name', ]
    list_editable = ['is_host', ]
    list_filter = ['click_num', 'sold_num', 'fav_num', 'good_nums', 'market_price',
                   'shop_price', 'is_new', 'is_hot']
    style_fields = {"goods_des": "ueditor"}

    class GoodsImage(object):
        # 小轮播图GoodsAdmin
        model = GoodsImage
        extra = 0
        relfield_style = 'fk-ajax'

    inlines = [GoodsImage, ]


class CarouselAdmin(object):
    # 大轮播图
    list_display = ['goods', 'image', 'index', 'add_time']
    relfield_style = 'fk-ajax'


class HotSearchWordsAdmin(object):
    list_display = ['keywords', 'index', 'add_time']


class IndexAdAdmin(object):
    # 首页商品类别广告
    list_display = ["goods"]
    relfield_style = 'fk-ajax'


xadmin.site.register(GoodsType, GoodTypeAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Carousel, CarouselAdmin)
xadmin.site.register(HotSearchWords, HotSearchWordsAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)
