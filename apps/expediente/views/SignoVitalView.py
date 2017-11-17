from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.SignoVitalRequest import SignoVitalForm
from apps.expediente.models import SignoVital

def registrarSignoVital(request):
	if request.method == 'POST':
		form = SignoVitalForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:listado_signos_vitales')
	else:
		form = SignoVitalForm()
	return render(
		request,
		'expediente/signos_vitales/registrar.html',
		{
			'form': form
		}
	)

def listadoSignosVitales(request):
	return render(
		request,
		'expediente/signos_vitales/listado.html',
		{
			'signos_vitales': SignoVital.objects.all()
		}
	)
