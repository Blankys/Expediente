from django.http import Http404, JsonResponse
from django.shortcuts import render
from apps.expediente.models import CatalogoMunicipio

def index(request):
    return render(request, 'expediente/inicio.html')

def municipios(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if request.method == 'GET':
        municipios = CatalogoMunicipio.objects.get(CatalogoDepartamento_id=id)
        return JsonResponse({'error': False, 'municipios': municipios})
    return JsonResponse({'error': True, 'municipios': ''})
