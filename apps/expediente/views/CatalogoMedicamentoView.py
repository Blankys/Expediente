from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from apps.expediente.permisos import Permisos
from apps.expediente.requests.CatalogoMedicamentoRequest import CatalogoMedicamentoForm
from apps.expediente.models import CatalogoMedicamento

class ListadoMedicamentos(ListView):
    model = CatalogoMedicamento
    template_name = 'expediente/medicamentos/listado.html'

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ListadoMedicamentos, self).dispatch(*args, **kwargs)

class AgregarMedicamento(CreateView):
    model = CatalogoMedicamento
    form_class = CatalogoMedicamentoForm
    template_name = 'expediente/medicamentos/formulario.html'
    success_url = reverse_lazy('expediente:listado_medicamentos')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(AgregarMedicamento, self).dispatch(*args, **kwargs)

class ModificarMedicamento(UpdateView):
    model = CatalogoMedicamento
    form_class = CatalogoMedicamentoForm
    template_name = 'expediente/medicamentos/formulario.html'
    success_url = reverse_lazy('expediente:listado_medicamentos')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ModificarMedicamento, self).dispatch(*args, **kwargs)

def eliminarMedicamento(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if Permisos.solo_admin:
        return JsonResponse({'error': True, 'mensaje': 'Usted no tiene permiso para realizar esta acción'})
    medicamento = CatalogoMedicamento.objects.get(id = id)
    if request.method == 'GET':
        medicamento.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Medicamento ' + medicamento.nombreMedicamento})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Medicamento ' + medicamento.nombreMedicamento})
