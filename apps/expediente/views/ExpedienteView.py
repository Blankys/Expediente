from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.expediente.requests.ExpedienteRequest import *
from apps.expediente.models import Expediente

class listadoExpedientes(ListView):
    model = Expediente
    template_name = 'expediente/expedientes/listado.html'

def registrarExpediente(request):
    if request.method == 'POST':
        direccion_paciente_form = DireccionForm(request.POST, prefix='paciente')
        persona_paciente_form = PersonaForm(request.POST, prefix='paciente')
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        expediente_form = ExpedienteForm(request.POST, prefix='paciente')

        if direccion_paciente_form.is_valid():
            direccion_paciente_form.save()

            if persona_paciente_form.is_valid():
                paciente_form.data['Direccion'] = direccion_paciente_form.id
                persona_paciente_form.save()

                if paciente_form.is_valid():
                    paciente_form.data['Persona'] = persona_paciente_form.id
                    paciente_form.data['Clinica'] = 1
                    paciente_form.save()

                    if expediente_form.is_valid():
                        expediente_form.data['Paciente'] = paciente_form.id
                        expediente_form.data['Clinica'] = 1
                        expediente_form.save()
                        return redirect('expediente:listado_expedientes')
    else:
        direccion_paciente_form = DireccionForm(request.POST, prefix='paciente')
        persona_paciente_form = PersonaForm(request.POST, prefix='paciente')
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        expediente_form = ExpedienteForm(request.POST, prefix='paciente')

    return render(
        request,
        'expediente/expedientes/formulario.html',
        {
            'direccion_paciente': direccion_paciente_form,
            'persona_paciente': persona_paciente_form,
            'paciente': paciente_form,
            'expediente': expediente_form
        }
    )

def modificarExpediente(request, id):
    expediente = Expediente.objects.get(id=id)

    if request.method == 'GET':
        direccion_paciente_form = DireccionForm(prefix='paciente', instance=expediente.Paciente.Persona.Direccion)
        persona_paciente_form = PersonaForm(prefix='paciente', instance=expediente.Paciente.Persona)
        paciente_form = PacienteForm(prefix='paciente', instance=expediente.Paciente)
        expediente_form = ExpedienteForm(prefix='paciente', instance=expediente)
    else:
        direccion_paciente_form = DireccionForm(request.POST, prefix='paciente', instance=expediente.Paciente.Persona.Direccion)
        persona_paciente_form = PersonaForm(request.POST, prefix='paciente', instance=expediente.Paciente.Persona)
        paciente_form = PacienteForm(request.POST, prefix='paciente', instance=expediente.Paciente)
        expediente_form = ExpedienteForm(request.POST, prefix='paciente', instance=expediente)

        if direccion_paciente_form.is_valid():
            direccion_paciente_form.save()

            if persona_paciente_form.is_valid():
                paciente_form.data['Direccion'] = direccion_paciente_form.id
                persona_paciente_form.save()

                if paciente_form.is_valid():
                    paciente_form.data['Persona'] = persona_paciente_form.id
                    paciente_form.data['Clinica'] = 1
                    paciente_form.save()

                    if expediente_form.is_valid():
                        expediente_form.data['Paciente'] = paciente_form.id
                        expediente_form.data['Clinica'] = 1
                        expediente_form.save()
                        return redirect('expediente:listado_expedientes')

    return render(
        request,
        'expediente/expedientes/formulario.html',
        {
            'direccion_paciente': direccion_paciente_form,
            'persona_paciente': persona_paciente_form,
            'paciente': paciente_form,
            'expediente': expediente_form
        }
    )

def eliminarExpediente(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    expediente = Expediente.objects.get(id = id)
    if request.method == 'GET':
        expediente.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Expediente ' + expediente.Paciente.Persona.nombreCompleto()})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Expediente ' + expediente.Paciente.Persona.nombreCompleto()})
