from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import render
from apps.expediente.models import CatalogoMunicipio

def index(request):
    return render(request, 'expediente/inicio.html')

def municipios(request):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    id = request.GET.get('id', None)
    try:
        municipios = CatalogoMunicipio.objects.filter(CatalogoDepartamento_id=id)
        return HttpResponse(serializers.serialize('json', municipios), content_type="application/json")
    except CatalogoMunicipio.DoesNotExist:
        return HttpResponse(serializers.serialize('json', []), content_type="application/json")
