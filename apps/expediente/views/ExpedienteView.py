from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.ExpedienteRequest import *
from apps.expediente.models import Expediente

def registrarExpediente(request):
    if (request.method == 'POST'):
        form1 = PersonaForm(request.POST)
        form2 = PacienteForm(request.POST)
        form3 = ExpedienteForm(request.POST)
        if form1.is_valid():
            persona = form1.save()
        else:
            form1 = PersonaForm()
        form2.data = form2.data.copy()
        form2.data['Persona'] = persona.id
        if form2.is_valid():
            paciente = form2.save()
        else:
            from2 = PacienteForm()
        form3.data = form3.data.copy()
        form3.data['Paciente'] = paciente.id
        if form3.is_valid():
            form3.save()
            return redirect('/')
        else:
            form = PacienteForm()
    return render(
        request,
        'expediente/expedientes/registrar.html',
        {
            'form1': PersonaForm,
            'form2': PacienteForm,
            'form3': ExpedienteForm
        }
)

def listadoExpediente(request):
    if (request.method == 'POST'):
        busquedaId = request.POST['Busqueda']
        try:
            expediente = Expediente.objects.get(id=busquedaId)
        except Expediente.DoesNotExist:
            expediente = None
        return render(
            request,
            'expediente/expedientes/listado.html',
            {
                'exp' : expediente
            }
        )

    return render(
		request,
		'expediente/expedientes/listado.html',
	)

