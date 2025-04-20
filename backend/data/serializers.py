from rest_farmework import serializers
from .models import *

class SupermarketSalesSerializers(models.ModelSerializer):
    #new comment


    
    class meta:
        model = SuperMarketSales
        field =('id', 'unit_price', 'date','country','gender','customer_type','product_line','payment','brranch')



#najmou nektbou hakka bech nadouhom lkol fi blaset ma nab9ou nektbou fihom lkol '__all__' fi field akid