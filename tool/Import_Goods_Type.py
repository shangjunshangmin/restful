# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/9 0009 下午 9:49'
import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restful_f.settings")

import django

django.setup()
from goods.models import GoodsType
from tool.data.Goods_Type import row_data

for level1_good in row_data:
    obj1 = GoodsType()
    status = GoodsType.objects.filter(code =level1_good['code'],name=level1_good['name']).first()
    if status:
        print('已经存在')
    else:
        obj1.code = level1_good['code']
        obj1.name = level1_good['name']
        obj1.category_type = 1
        obj1.save()
        for level2_good in level1_good['sub_categorys']:
            obj2 = GoodsType()
            obj2.code = level2_good['code']
            obj2.name = level2_good['name']
            obj2.category_type = 2
            obj2.parent_type = obj1
            obj2.save()
            for level3_good in level2_good['sub_categorys']:
                obj3 = GoodsType()
                obj3.code = level3_good['code']
                obj3.name = level3_good['name']
                obj3.category_type = 3
                obj3.parent_type = obj2
                obj3.save()
