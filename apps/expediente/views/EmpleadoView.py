from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.EmpleadoRequest import EmpleadoForm, PersonaForm
from apps.expediente.models import Empleado

class listadoEmpleados(ListView):
    model = Empleado
    template_name = 'expediente/empleados/listado.html'

def agregarEmpleado(request):
	if request.method == 'POST':
		persona_form = PersonaForm(request.POST)
		empleado_form = EmpleadoForm(request.POST)
		if persona_form.is_valid():
			persona_form.save()
		if empleado_form.is_valid():
			empleado_form.data['Persona'] = persona_form.id
			empleado_form.save()
		return redirect('expediente:listado_empleados')
	else:
		persona_form = PersonaForm()
		empleado_form = EmpleadoForm()
	return render(request, 'expediente/empleados/formulario.html', {'persona': persona_form, 'empleado': empleado_form})

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
class agregarEmpleado(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'expediente/empleados/formulario.html'
	success_url = reverse_lazy('expediente:listado_empleados')

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
