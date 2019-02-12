from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import filters

from .models import Goods,GoodsCategory,Test
from .serializers import GoodsSerializer,CategorySerializer3,TestSerializer
from .permissions import CustomerAccessPermission

from .filters import GoodsFilter
# Create your views here.

'''
class GoodsListViewSet(mixins.ListModelMixin,GenericViewSet):

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class=GoodsFilter
    search_fields=("name","goods_desc")
    ordering_fields=("sold_num","add_time")
'''

class CategoryViewset(mixins.DestroyModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer3


class TestViewset(mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = TestSerializer
    permission_classes = (CustomerAccessPermission,)

    queryset = Test.objects.all()