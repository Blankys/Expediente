from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.ReferenciaMedicaRequest import ReferenciaMedicaForm
from apps.expediente.models import ReferenciaMedica

def registrarReferenciaMedica(request):
	if request.method == 'POST':
		form = ReferenciaMedicaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:index')
	else:
		form = ReferenciaMedicaForm()
	return render(request,'expediente/referencia_medica/registrar.html',{'form': form})

def listadoReferenciaMedica(request):
	return render(request,'expediente/referencia_medica/listado.html',{'referencias_medicas': ReferenciaMedica.objects.all()})