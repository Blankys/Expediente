from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.IncapacidadMedicaRequest import IncapacidadForm
from apps.expediente.models import IncapacidadMedica


class ListadoIncapacidadesMedicas(ListView):
    model = IncapacidadMedica
    template_name = 'expediente/incapacidad/listado.html'

class AgregarIncapacidadMedica(CreateView):
    model = IncapacidadMedica
    form_class = IncapacidadForm
    template_name = 'expediente/incapacidad/formulario.html'
    success_url = reverse_lazy('expediente:listado_incapacidades')

class ModificarIncapacidadMedica(UpdateView):
    model = IncapacidadMedica
    form_class = IncapacidadForm
    template_name = 'expediente/incapacidad/formulario.html'
    success_url = reverse_lazy('expediente:listado_incapacidades')


def eliminarIncapacidad(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    incapacidad = IncapacidadMedica.objects.get(id = id)

    if request.method == 'GET':
        incapacidad.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la incapacidad medica de ' + incapacidad.Expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la incapacidad medica de ' + incapacidad.Expediente.Paciente.Persona.nombreCompleto()})
