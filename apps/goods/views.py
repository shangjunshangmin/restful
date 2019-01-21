from .serializers import GoodsSerializer, GoodsTypeSerializer
from .filters import GoodFilter
from rest_framework import mixins
from .models import Goods, GoodsType
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication


class GoodPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


class GoodsList(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    列出所有的商品分页、搜索、过滤、排序
    """

    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodPagination
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'shop_price')
    ordering_fields = ('shop_price','sold_num')
    filter_class = GoodFilter


class GoodsTypeList(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
       列出所有的商品分类
    """

    queryset = GoodsType.objects.filter(category_type=1).all()
    serializer_class = GoodsTypeSerializer
