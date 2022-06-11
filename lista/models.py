from django.db import models


class Lista(models.Model):
    nome_item = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    observacao = models.TextField(max_length=200, blank=True)

