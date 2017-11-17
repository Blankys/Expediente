from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.EmpleadoRequest import EmpleadoForm, PersonaForm
from apps.expediente.models import Empleado

def registrarEmpleado(request):
	if request.method == 'POST':
		persona = PersonaForm(request.POST)
		empleado = EmpleadoForm(request.POST)
		if persona.is_valid():
			persona.save()
		if empleado.is_valid():
			empleado.data['Persona'] = persona.id
			empleado.save()
		return redirect('expediente:listado_empleados')
	else:
		persona = PersonaForm()
		empleado = EmpleadoForm()
	return render(
		request,
		'expediente/empleados/registrar.html',
		{
			'persona': persona,
			'empleado': empleado
		}
	)

def listadoEmpleados(request):
	return render(
		request,
		'expediente/empleados/listado.html',
		{
			'empleados': Empleado.objects.all()
		}
	)
