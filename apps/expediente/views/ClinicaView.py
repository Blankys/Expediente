from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.ClinicaRequest import ClinicaForm
from apps.expediente.models import Clinica


class ListadoClinica(ListView):
    model = Clinica
    template_name = 'expediente/clinicas/listado.html'

class AgregarClinica(CreateView):
    model = Clinica
    form_class = ClinicaForm
    template_name = 'expediente/clinicas/formulario.html'
    success_url = reverse_lazy('expediente:listado_clinicas')

class ModificarClinica(UpdateView):
    model = Clinica
    form_class = ClinicaForm
    template_name = 'expediente/clinicas/formulario.html'
    success_url = reverse_lazy('expediente:listado_clinicas')


def eliminarClinica(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    clinica = Clinica.objects.get(id = id)
    if request.method == 'GET':
        clinica.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Clinica: ' + clinica.Clinica})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Clinica ' + clinica.Clinica})
