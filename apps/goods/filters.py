# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/19 0019 下午 11:29'

from django_filters import rest_framework as filters
from .models import Goods


class GoodFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="market_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="market_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price']