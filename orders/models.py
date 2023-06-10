from django.contrib.auth.models import User
from django.db import models


# Pedido


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('Item', related_name='orders')

    def __str__(self):
        return f'Pedido do usuário {self.user} realizado em {self.created_at}'


# Item


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name