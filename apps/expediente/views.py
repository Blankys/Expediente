from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests import ResultadoExamenForm
from apps.expediente.models import ResultadoExamen

def index(request):
	return render(request, 'expediente/inicio.html')

"""
Vista que redirecciona al template: expediente/registrar_resultado
Qué contiene el formulario para registrar el resultado de un examen de laboratorio
"""
def registrarResultadoExamen(request):
	if request.method == 'POST':
		form = ResultadoExamenForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:index')
	else:
		form = ResultadoExamenForm()
	return render(
		request,
		'expediente/examenes/registrar.html',
		{
			'form': form
		}
	)

def listadoExamenes(request):
	return render(
		request,
		'expediente/examenes/listado.html',
		{
			'examenes': ResultadoExamen.objects.all()
		}
	)
