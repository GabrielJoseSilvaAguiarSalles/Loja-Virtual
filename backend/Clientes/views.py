from django.http import JsonResponse

from .models import Cliente

def listar_clientes(request):
    Cliente = Cliente.object.all().values('id', 'nome', 'email', 'data_cadastro')
    return JsonResponse(list(Cliente), safe=False)