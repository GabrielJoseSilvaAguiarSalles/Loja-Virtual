from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=128)

    def __str__(self):
        return self.nome