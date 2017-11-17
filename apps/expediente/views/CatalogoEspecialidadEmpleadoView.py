from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.CatalogoEspecialidadEmpleadoRequest import CatalogoEspecialidadEmpleadoForm
from apps.expediente.models import CatalogoEspecialidadEmpleado

def registrarCatalogoEspecialidadEmpleado(request):
	if request.method == 'POST':
		form = CatalogoEspecialidadEmpleadoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:listado_especialidades_empleados')
	else:
		form = CatalogoEspecialidadEmpleadoForm()
	return render(
		request,
		'expediente/especialidades-empleados/registrar.html',
		{
			'form': form
		}
	)

def listadoCatalogoEspecialidadEmpleados(request):
	return render(
		request,
		'expediente/especialidades-empleados/listado.html',
		{
			'especialidades_empleados': CatalogoEspecialidadEmpleado.objects.all()
		}
	)
