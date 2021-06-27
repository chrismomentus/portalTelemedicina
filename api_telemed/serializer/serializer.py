from rest_framework import serializers
from api_telemed.models.models import *

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Order
        fields = '__all__'
