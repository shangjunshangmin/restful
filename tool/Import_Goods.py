# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/10 0010 下午 1:17'
import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restful_f.settings")
import django

django.setup()
from goods.models import Goods, GoodsImage, GoodsType
from tool.data.Goods import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
    goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_des = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

    goods_detail_name = goods_detail["categorys"][-1]
    category = GoodsType.objects.filter(name=goods_detail_name).first()
    if category:
        goods.type = category
    goods.save()

    for goods_image in goods_detail["images"]:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()

