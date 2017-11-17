from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.CatalogoMedicamentoRequest import CatalogoMedicamentoForm
from apps.expediente.models import CatalogoMedicamento

def registrarCatalogoMedicamento(request):
	if request.method == 'POST':
		form = CatalogoMedicamentoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:listado_medicamentos')
	else:
		form = CatalogoMedicamentoForm()
	return render(
		request,
		'expediente/medicamentos/registrar.html',
		{
			'form': form
		}
	)

def listadoCatalogoMedicamentos(request):
	return render(
		request,
		'expediente/medicamentos/listado.html',
		{
			'medicamentos': CatalogoMedicamento.objects.all()
		}
	)
