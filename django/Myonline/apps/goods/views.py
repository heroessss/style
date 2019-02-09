from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
from .serializers import GoodsSerializer
# Create your views here.
class GoodListView(APIView):
    def get(self,request):
        goods=Goods.objects.all()
        serializer=GoodsSerializer(goods,many=True)
        return Response(serializer.data)
