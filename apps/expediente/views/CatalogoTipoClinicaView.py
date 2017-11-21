from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from apps.expediente.permisos import Permisos
from apps.expediente.requests.CatalogoTipoClinicaRequest import CatalogoTipoClinicaForm
from apps.expediente.models import CatalogoTipoClinica


class ListadoTipoClinicas (ListView):
    model = CatalogoTipoClinica
    template_name = 'expediente/clinicas/tipos/listado.html'

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ListadoTipoClinicas, self).dispatch(*args, **kwargs)


class AgregarTipoClinica (CreateView):
    model = CatalogoTipoClinica
    form_class = CatalogoTipoClinicaForm
    template_name = 'expediente/clinicas/tipos/formulario.html'
    success_url = reverse_lazy('expediente:listado_tipo_clinicas')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(AgregarTipoClinica, self).dispatch(*args, **kwargs)


class ModificarTipoClinica (UpdateView):
    model = CatalogoTipoClinica
    form_class = CatalogoTipoClinicaForm
    template_name = 'expediente/clinicas/tipos/formulario.html'
    success_url = reverse_lazy('expediente:listado_tipo_clinicas')

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ModificarTipoClinica, self).dispatch(*args, **kwargs)


def eliminarTipoClinica(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if Permisos.solo_admin:
        return JsonResponse({'error': True, 'mensaje': 'Usted no tiene permiso para realizar esta acción'})
    tipo_clinica = CatalogoTipoClinica.objects.get(id = id)
    if request.method == 'GET':
        tipo_clinica.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó el tipo de clinica' + tipo_clinica.tipoClinica})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar el tipo de clinica ' + tipo_clinica.tipoClinica})
