from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.ReferenciaMedicaRequest import ReferenciaMedicaForm
from apps.expediente.models import ReferenciaMedica


class listadoReferenciaMedica(ListView):
    model = ReferenciaMedica
    template_name = 'expediente/referencias/listado.html'

class registrarReferenciaMedica(CreateView):
    model = ReferenciaMedica
    form_class = ReferenciaMedicaForm
    template_name = 'expediente/referencias/formulario.html'
    success_url = reverse_lazy('expediente:listado_referencia_medica')

class ModificarReferenciaMedica(UpdateView):
    model = ReferenciaMedica
    form_class = ReferenciaMedicaForm
    template_name = 'expediente/referencias/formulario.html'
    success_url = reverse_lazy('expediente:listado_referencia_medica')


def eliminarReferencia(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    referencia = ReferenciaMedica.objects.get(id = id)

    if request.method == 'GET':
        referencia.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la referencia medica de ' + referencia.Expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la referencia medica de ' + referencia.Expediente.Paciente.Persona.nombreCompleto()})
