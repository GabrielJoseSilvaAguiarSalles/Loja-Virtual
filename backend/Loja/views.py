from django.http import JsonResponse

from .models import Loja

def listar_lojas(request):
    Loja = Loja.object.all().values('id', 'nome', 'localizacao')
    return JsonResponse(list(Loja), safe=False)
