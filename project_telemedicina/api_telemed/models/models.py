from django.db import models
from django.contrib.auth.models import User

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=200)    
    data_criado = models.DateField()

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome

class Order(models.Model):
    product_order = models.ForeignKey(produto, on_delete=models.CASCADE)
    user_order = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.user_order.nome)
