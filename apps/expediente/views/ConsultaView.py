from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.ConsultaRequest import ConsultaForm
from apps.expediente.models import Consulta


class ListadoConsultas(ListView):
    model = Consulta
    template_name = 'expediente/consulta/listado.html'

class RegistrarConsulta(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'expediente/consulta/formulario.html'
    success_url = reverse_lazy('expediente:listado_consultas')

class ModificarConsulta(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'expediente/consulta/formulario.html'
    success_url = reverse_lazy('expediente:listado_consultas')


def eliminarConsulta(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    consulta = Consulta.objects.get(id = id)
    if request.method == 'GET':
        consulta.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Consulta de ' + consulta.Expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la consulta de ' + consulta.Expediente.Paciente.Persona.nombreCompleto()})
