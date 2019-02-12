# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
from .models import Goods

class GoodsFilter(filters.FilterSet):
    '''
    商品过滤器
    '''
    price_min=filters.NumberFilter(field_name="shop_price",lookup_expr="gte")
    name=filters.CharFilter(field_name="name",lookup_expr="icontains")

    class Meta:
        model=Goods
        fields =["price_min","name"]