from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.TurnoRequest import TurnoForm
from apps.expediente.models import Turno


class ListadoTurnos(ListView):
    model = Turno
    template_name = 'expediente/turnos/listado.html'

class AgregarTurno(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'expediente/turnos/formulario.html'
    success_url = reverse_lazy('expediente:listado_turnos')

class ModificarTurno(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'expediente/turnos/formulario.html'
    success_url = reverse_lazy('expediente:listado_turnos')


def eliminarTurno(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    turno = Turno.objects.get(id = id)
    if request.method == 'GET':
        turno.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó el turno.'})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar el turno.'})
