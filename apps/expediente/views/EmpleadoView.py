from django.http import Http404, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.EmpleadoRequest import EmpleadoForm, PersonaForm
from apps.expediente.models import Empleado

class listadoEmpleados(ListView):
    model = Empleado
    template_name = 'expediente/empleados/listado.html'

class agregarEmpleado(CreateView):
	model = Empleado
	template_name = 'expediente/empleados/formulario.html'
	form_class = EmpleadoForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('expediente:listado_empleados')

	def get_context_data(self, **kwargs):
		context = super(agregarEmpleado, self).get_context_data(**kwargs)
		if 'empleado' not in context:
			context['empleado'] = self.form_class(self.request.GET)
		if 'persona' not in context:
			context['persona'] = self.second_form_class(self.request.GET)
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
			return self.render_to_response(self.get_context_data(empleado=empleado_form, persona=persona_form))

def modificarEmpleado(request, id):
	empleado = Empleado.objects.get(id=id)
	persona = empleado.Persona
	if request.method == 'GET':
		empleado_form = EmpleadoForm(instance = empleado)
		persona_form = PersonaForm(instance = persona)
	else:
		empleado_form = EmpleadoForm(request.POST, instance = empleado)
		persona_form = PersonaForm(request.POST, instance = persona)
		if persona_form.is_valid():
			persona_form.save()
		if empleado_form.is_valid():
			empleado_form.data['Persona'] = persona_form.id
			empleado_form.save()
		return redirect('expediente:listado_empleados')
	return render(request, 'expediente/empleados/formulario.html', {'persona': persona_form, 'empleado': empleado_form})

'''
class modificarEmpleado(UpdateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'expediente/empleados/formulario.html'
	success_url = reverse_lazy('expediente:listado_empleados')
'''

def eliminarEmpleado(request, id):
	if not request.is_ajax():
		raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
	empleado = Empleado.objects.get(id = id)
	if request.method == 'GET':
		empleado.delete()
		return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Empleado ' + empleado.Persona.nombreCompleto()})
	return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Empleado ' + empleado.Persona.nombreCompleto()})
