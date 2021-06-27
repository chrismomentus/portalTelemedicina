
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api_telemed.views import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', productViewset, basename="products")
router.register(r'orders', orderViewset, basename="orders")



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('api_telemed.urls')),
    path('signup/', include('rest_auth.registration.urls')),    
    path('login/', include('rest_framework.urls', namespace="rest_framework")),
    path('product/(?P<pk>[0-9]+)/', Delete_Put_Product.as_view(),name='Delete_Put_product'),
]
