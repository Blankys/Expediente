from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from apps.expediente.permisos import Permisos
from apps.expediente.requests.CatalogoEspecialidadEmpleadoRequest import CatalogoEspecialidadEmpleadoForm
from apps.expediente.models import CatalogoEspecialidadEmpleado

class ListadoEspecialidadesEmpleados(ListView):
    model = CatalogoEspecialidadEmpleado
    template_name = 'expediente/empleados/especialidades/listado.html'

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ListadoEspecialidadesEmpleados, self).dispatch(*args, **kwargs)

class AgregarEspecialidadEmpleado(CreateView):
    model = CatalogoEspecialidadEmpleado
    form_class = CatalogoEspecialidadEmpleadoForm
    template_name = 'expediente/empleados/especialidades/formulario.html'
    success_url = reverse_lazy('expediente:listado_especialidades_empleados')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(AgregarEspecialidadEmpleado, self).dispatch(*args, **kwargs)

class ModificarEspecialidadEmpleado(UpdateView):
    model = CatalogoEspecialidadEmpleado
    form_class = CatalogoEspecialidadEmpleadoForm
    template_name = 'expediente/empleados/especialidades/formulario.html'
    success_url = reverse_lazy('expediente:listado_especialidades_empleados')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ModificarEspecialidadEmpleado, self).dispatch(*args, **kwargs)

def eliminarEspecialidadEmpleado(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if Permisos.solo_admin:
        return JsonResponse({'error': True, 'mensaje': 'Usted no tiene permiso para realizar esta acción'})
    especialidad_empleado = CatalogoEspecialidadEmpleado.objects.get(id = id)
    if request.method == 'GET':
        especialidad_empleado.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Especialidad Empleado ' + especialidad_empleado.tipoEspecialidad})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Especialidad Empleado ' + especialidad_empleado.tipoEspecialidad})
