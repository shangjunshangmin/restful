# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2018/12/19 0019 下午 11:29'

from django_filters import rest_framework as filters
from .models import Goods
from django.db.models import Q


class GoodFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(field_name="market_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="market_price", lookup_expr='lte')
    top_category = filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(type__id=value) | Q(type__parent_type__id=value) | Q(type__parent_type__parent_type__id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
