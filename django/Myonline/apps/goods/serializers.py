# -*- coding: utf-8 -*-
from rest_framework import serializers

from goods.models import Goods

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("__all__")
    # def validate_code(self,code):
    #     if len(code)<5:
    #         raise serializers.ValidationError("hahha")
