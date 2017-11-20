from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.CatalogoTipoClinicaRequest import CatalogoTipoClinicaForm
from apps.expediente.models import CatalogoTipoClinica


class ListadoTipoClinicas (ListView):
    model = CatalogoTipoClinica
    template_name = 'expediente/clinicas/especialidades/listado.html'


class AgregarTipoClinica (CreateView):
    model = CatalogoTipoClinica
    form_class = CatalogoTipoClinicaForm
    template_name = 'expediente/clinicas/especialidades/formulario.html'
    success_url = reverse_lazy('expediente:listado_tipo_clinicas')


class ModificarTipoClinica (UpdateView):
    model = CatalogoTipoClinica
    form_class = CatalogoTipoClinicaForm
    template_name = 'expediente/clinicas/especialidades/formulario.html'
    success_url = reverse_lazy('expediente:listado_tipo_clinicas')


def eliminarTipoClinica(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    tipo_clinica = CatalogoTipoClinica.objects.get(id = id)
    if request.method == 'GET':
        tipo_clinica.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó el tipo de clinica' + tipo_clinica.tipoClinica})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar el tipo de clinica ' + tipo_clinica.tipoClinica})
