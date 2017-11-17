from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.CatalogoEnfermedadRequest import CatalogoEnfermedadForm
from apps.expediente.models import CatalogoEnfermedad

def registrarCatalogoEnfermedad(request):
	if request.method == 'POST':
		form = CatalogoEnfermedadForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:listado_enfermedades')
	else:
		form = CatalogoEnfermedadForm()
	return render(
		request,
		'expediente/enfermedades/registrar.html',
		{
			'form': form
		}
	)

def listadoCatalogoEnfermedads(request):
	return render(
		request,
		'expediente/enfermedades/listado.html',
		{
			'enfermedades': CatalogoEnfermedad.objects.all()
		}
	)
