#from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


from .serializers import BrendSerializer
#from rest_framework.permissions import AllowAny

from kompany.models import Brend


class BrendAPIView(APIView):
    def get(self, request):
        brend = Brend.objects.all()
        return Response({'brends': BrendSerializer(brend, many=True).data})
    

#если тедать api через сериализатор
# class ProductAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class BrendAPIView(generics.ListCreateAPIView):
#     queryset = Brend.objects.all()
#     serializer_class = BrendSerializer


    


