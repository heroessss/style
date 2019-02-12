# -*- coding: utf-8 -*-
from rest_framework import serializers

from goods.models import Goods,GoodsCategory,Test

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("__all__")

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ("__all__")

class CategorySerializer2(serializers.ModelSerializer):
    sub_cat=CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = ("__all__")

class CategorySerializer(serializers.ModelSerializer):
    sub_cat=CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = ("__all__")

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("__all__")