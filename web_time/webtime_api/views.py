from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from kompany.models import Product, Brend
from .serializers import ProductSerializer, BrendSerializer

from rest_framework.permissions import AllowAny


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrendAPIView(generics.ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

#Product 
# class ProductAPIView(APIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # анонимные пользователи могут делать только get

#     def get_queryset(self):
#         return Product.objects.all()

#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response({'products': serializer.data})
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"ошибка": "метод put не определен"})
        
#         try:
#             instance = Product.objects.get(pk=pk)
#         except:
#             return Response({"ошибка": "объект не найден"})
        
#         serializer = ProductSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


# Brend   

    


