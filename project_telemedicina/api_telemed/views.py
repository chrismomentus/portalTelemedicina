from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics, authentication 
from api_telemed.serializer.serializer import productSerializer, orderSerializer
from api_telemed.models.models import produto, Order
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
#@api_view()
@permission_classes([AllowAny])
def home(request):
    return render(request, 'home.html', {})

#@api_view()
@permission_classes([IsAuthenticated])
class Delete_Put_Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = produto.objects.all()
    serializer_class = productSerializer
    authentication_classes = [authentication.SessionAuthentication]
    


@permission_classes([AllowAny])
class productViewset(viewsets.ModelViewSet):
    serializer_class = productSerializer    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['preco', 'data_criado']
    def get_queryset(self):
        queryset = produto.objects.all()
        return queryset

class orderViewset(viewsets.ModelViewSet):
    serializer_class = orderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_order', 'user_order']
    def get_queryset(self):
        queryset= Order.objects.all()
        return queryset

