from django.http import JsonResponse

from .models import Produto

def listar_produtos(request):
    Produto = Produto.object.all().values('id', 'nome', 'localizacao')
    return JsonResponse(list(Produto), safe=False)
