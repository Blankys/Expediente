from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.ConstanciaMedicaRequest import ConstanciaForm
from apps.expediente.models import ConstanciaMedica


class ListadoConstanciasMedicas(ListView):
    model = ConstanciaMedica
    template_name = 'expediente/constancias/listado.html'

class AgregarConstanciaMedica(CreateView):
    model = ConstanciaMedica
    form_class = ConstanciaForm
    template_name = 'expediente/constancias/formulario.html'
    success_url = reverse_lazy('expediente:listado_constancias')

class ModificarConstanciaMedica(UpdateView):
    model = ConstanciaMedica
    form_class = ConstanciaForm
    template_name = 'expediente/constancia/formulario.html'
    success_url = reverse_lazy('expediente:listado_constancias')


def eliminarConstancia(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    constancia = ConstanciaMedica.objects.get(id = id)
    if request.method == 'GET':
        constancia.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la constancia medica de ' + constancia.Expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la constancia medica de ' + constancia.Expediente.Paciente.Persona.nombreCompleto()})
