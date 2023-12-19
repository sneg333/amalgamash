from django.urls import path
from . import views


urlpatterns = [
    path('v1/products/', views.ProductAPIView.as_view(), name='products'),
    path('v1/products/<int:pk>', views.ProductAPIView.as_view(), name='put'),


    path('v1/brends/', views.BrendAPIView.as_view(), name='brends'),
]