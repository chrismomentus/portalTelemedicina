from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', productViewset, basename="products")
router.register(r'orders', orderViewset, basename="orders")


urlpatterns = [
    path('home/', views.home, name="home"),
    path('product/(?P<pk>[0-9]+)/', Delete_Put_Product.as_view(),name='Delete_Put_product'),
    path('', include(router.urls)),
]