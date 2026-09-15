from django.contrib import admin
from .models import Produto
admin.site.register(Produto)
#As entidades Clientes e Produtos possuem um relacionamento de N:N, porque um cliente pode comprar diversos produtos, assim como um mesmo tipo de produto pode ser
#comprado por diversos clientes.