from django.urls import path
from webtime_api.views import BrendAPIView


urlpatterns = [
path('v1/brends/', BrendAPIView.as_view()),
#     path('v1/products/<int:pk>', views.ProductAPIView.as_view(), name='put'),


#    path('v1/brends/', views.BrendAPIView.as_view(), name='brends'),
]