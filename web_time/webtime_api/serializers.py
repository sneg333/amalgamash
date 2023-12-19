from rest_framework import serializers
from kompany.models import Product, Brend



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'id')



class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('title', 'id')
