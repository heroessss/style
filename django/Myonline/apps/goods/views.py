from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Goods
from .serializers import GoodsSerializer
# Create your views here.
class GoodsListViewSet(mixins.ListModelMixin,GenericViewSet):
    '''
    商品详情页
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=("name","shop_price")