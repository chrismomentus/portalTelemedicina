from django.contrib import admin
from api_telemed.models.models import *
# Register your models here.


admin.register(produto, Order)(admin.ModelAdmin)