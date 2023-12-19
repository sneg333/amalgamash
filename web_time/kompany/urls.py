from django.urls import path
from kompany import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact/', views.contact, name='contact'),
    path('onas/', views.onas, name='onas'),

    path('brends/<int:id>/', views.pod_brand, name='pod_brand'),
    path('products/<int:id>/', views.products, name='products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    path('search/', views.search_view, name='search'),
]