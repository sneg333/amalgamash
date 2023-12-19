from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
]