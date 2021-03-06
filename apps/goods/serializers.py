# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/19 0019 下午 7:50'
from rest_framework import serializers
from .models import Goods, GoodsType, GoodsImage


class GoodsTypeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsTypeSerializer1(serializers.ModelSerializer):
    sub_cat = GoodsTypeSerializer2(many=True)

    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsTypeSerializer(serializers.ModelSerializer):
    sub_cat = GoodsTypeSerializer1(many=True)

    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    type = GoodsTypeSerializer()
    image = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"
