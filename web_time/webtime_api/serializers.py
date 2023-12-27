from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from kompany.models import Brend


class BrendSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    pod_brend = serializers.CharField(max_length=150)


#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('name', 'price', 'id')



# class BrendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brend
#         fields = ('title', 'id')
