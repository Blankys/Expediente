from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, HttpResponseRedirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from apps.expediente.permisos import Permisos
from apps.expediente.requests.EmpleadoRequest import EmpleadoForm, PersonaForm
from apps.expediente.models import Empleado, Persona

class ListadoEmpleados(ListView):
    model = Empleado
    template_name = 'expediente/empleados/listado.html'

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ListadoEmpleados, self).dispatch(*args, **kwargs)

class AgregarEmpleado(CreateView):
    model = Empleado
    template_name = 'expediente/empleados/formulario.html'
    form_class = EmpleadoForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('expediente:listado_empleados')

    def get_context_data(self, **kwargs):
        context = super(AgregarEmpleado, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        empleado_form = self.form_class(request.POST)
        persona_form = self.second_form_class(request.POST)
        if empleado_form.is_valid() and persona_form.is_valid():
            empleado = empleado_form.save(commit=False)
            empleado.Persona = persona_form.save()
            empleado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(
                form=empleado_form,
                form2=persona_form,
                empleado_errores=empleado_form.errors,
                persona_errores=persona_form.errors,
                mensaje_error='No se pudo guardar el Empleado. Por favor revise los datos.'
            ))

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(AgregarEmpleado, self).dispatch(*args, **kwargs)

class ModificarEmpleado(UpdateView):
    model = Empleado
    second_model = Persona
    form_class = EmpleadoForm
    second_form_class = PersonaForm
    template_name = 'expediente/empleados/formulario.html'
    success_url = reverse_lazy('expediente:listado_empleados')

    def get_context_data(self, **kwargs):
        context = super(ModificarEmpleado, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        empleado = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=empleado.Persona.id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_empleado = kwargs['pk']
        empleado = self.model.objects.get(id=id_empleado)
        persona = self.second_model.objects.get(id=empleado.Persona.id)
        empleado_form = self.form_class(request.POST, instance=empleado)
        persona_form = self.second_form_class(request.POST, instance=persona)
        if empleado_form.is_valid() and persona_form.is_valid():
            empleado_form.save()
            persona_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(Permisos.solo_admin, login_url='/acceso-denegado'))
    def dispatch(self, *args, **kwargs):
        return super(ModificarEmpleado, self).dispatch(*args, **kwargs)

def eliminarEmpleado(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    if Permisos.solo_admin:
        return JsonResponse({'error': True, 'mensaje': 'Usted no tiene permiso para realizar esta acción'})
    empleado = Empleado.objects.get(id = id)
    if request.method == 'GET':
        empleado.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Empleado ' + empleado.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Empleado ' + empleado.Persona.nombreCompleto()})
