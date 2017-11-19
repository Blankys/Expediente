from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.ExpedienteRequest import *
from apps.expediente.models import Expediente

def registrarExpediente(request):
    if (request.method == 'POST'):
        personaf = PersonaForm(request.POST, prefix='paciente')
        pacientef = PacienteForm(request.POST, prefix='paciente')
        expedientef = ExpedienteForm(request.POST, prefix='paciente')
        direccionf = DireccionForm(request.POST, prefix='paciente')
        contactoEf = ContactoEmergenciaForm(request.POST, prefix='contacto')
        contactoEDf = DireccionForm(request.POST, prefix='contacto')

        if direccionf.is_valid():
            direccionp = direccionf.save()
        else:
            direccionf = DireccionForm(prefix='paciente')
        personaf.data = personaf.data.copy()
        personaf.data['Direccion'] = direccionp.id
        if personaf.is_valid():
            persona = personaf.save()
        else:
            personaf = PacienteForm(prefix='paciente')
        pacientef.data = pacientef.data.copy()
        pacientef.data['Persona'] = persona.id
        if pacientef.is_valid():
            paciente = pacientef.save()
        else:
            pacientef = PacienteForm(prefix='paciente')
        expedientef.data = expedientef.data.copy()
        expedientef.data['Paciente'] = paciente.id
        if expedientef.is_valid():
            expediente = expedientef.save()
        else:
            expedientef = ExpedienteForm(prefix='paciente')
        if contactoEDf.is_valid():
            contactod = contactoEDf.save()
        else:
            contactoEDf = DireccionForm(prefix='contacto')
        contactoEf.data = contactoEf.data.copy()
        contactoEf.data['Direccion'] = contactod.id
        if contactoEf.is_valid():
            contactoEf.save()
        else:
            contactoEf = ContactoEmergenciaForm(prefix='contacto')
            return redirect('/')
    personaf = PersonaForm(prefix='paciente')
    pacientef = PacienteForm(prefix='paciente')
    expedientef = ExpedienteForm(prefix='paciente')
    direccionf = DireccionForm(prefix='paciente')
    contactoEf = ContactoEmergenciaForm(prefix='contacto')
    contactoEDf = DireccionForm(prefix='contacto')
    return render(
        request,
        'expediente/expedientes/registrar.html',
        {
            'form1': personaf,
            'form2': direccionf,
            'form3': pacientef,
            'form4': expedientef,
            'form5': contactoEf,
            'form6': contactoEDf
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

