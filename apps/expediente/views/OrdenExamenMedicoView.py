from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.ExamenMedicoRequest import OrdenExamenMedicoForm
from apps.expediente.models import OrdenExamenMedico

class ListadoOrdenesExamen(ListView):
    model = OrdenExamenMedico
    template_name = 'expediente/examenes/ordenes/listado.html'

class AgregarOrdenExamen(CreateView):
    model = OrdenExamenMedico
    form_class = OrdenExamenMedicoForm
    template_name = 'expediente/examenes/ordenes/formulario.html'
    success_url = reverse_lazy('expediente:listado_ordenes_examen')

class ModificarOrdenExamen(UpdateView):
    model = OrdenExamenMedico
    form_class = OrdenExamenMedicoForm
    template_name = 'expediente/examenes/ordenes/formulario.html'
    success_url = reverse_lazy('expediente:listado_ordenes_examen')


def eliminarOrdenExamen(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    ordenexamen = OrdenExamenMedico.objects.get(id = id)
    if request.method == 'GET':
        ordenexamen.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la orden de examen de ' + ordenexamen.Expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la orden de examen de ' + ordenexamen.Expediente.Paciente.Persona.nombreCompleto()})
