from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from apps.expediente.permisos import Permisos
from apps.expediente.requests.CatalogoEnfermedadRequest import CatalogoEnfermedadForm
from apps.expediente.models import CatalogoEnfermedad

class ListadoEnfermedades(ListView):
    model = CatalogoEnfermedad
    template_name = 'expediente/enfermedades/listado.html'

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ListadoEnfermedades, self).dispatch(*args, **kwargs)

class AgregarEnfermedad(CreateView):
    model = CatalogoEnfermedad
    form_class = CatalogoEnfermedadForm
    template_name = 'expediente/enfermedades/formulario.html'
    success_url = reverse_lazy('expediente:listado_enfermedades')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(AgregarEnfermedad, self).dispatch(*args, **kwargs)

class ModificarEnfermedad(UpdateView):
    model = CatalogoEnfermedad
    form_class = CatalogoEnfermedadForm
    template_name = 'expediente/enfermedades/formulario.html'
    success_url = reverse_lazy('expediente:listado_enfermedades')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ModificarEnfermedad, self).dispatch(*args, **kwargs)

def eliminarEnfermedad(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if Permisos.solo_admin:
        return JsonResponse({'error': True, 'mensaje': 'Usted no tiene permiso para realizar esta acción'})
    enfermedad = CatalogoEnfermedad.objects.get(id = id)
    if request.method == 'GET':
        enfermedad.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Enfermedad ' + enfermedad.nombreEnfermedad})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Enfermedad ' + enfermedad.nombreEnfermedad})
