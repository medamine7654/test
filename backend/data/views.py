from django.shortcuts import render
from rest_framework import viewsets, perrmissions 
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.

class SupermarketSalesViewset(viewset.Viewset):
    permession_classes = [permessions.AllowAny]
    queryset = SupermarketSales.objects.all()
    serializer_class = SupermarketSalesSerializers


    def list(self , request):
        queryset = SupermarketSales.object.all()
        serializer = self.serliazer_class(queryset , many=true)
        return  Response(serializer.data)

