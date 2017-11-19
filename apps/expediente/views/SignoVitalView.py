from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.SignoVitalRequest import SignoVitalForm
from apps.expediente.models import SignoVital

class listadoSignosVitales(ListView):
    model = SignoVital
    template_name = 'expediente/signos_vitales/listado.html'

class agregarSignoVital(CreateView):
    model = SignoVital
    form_class = SignoVitalForm
    template_name = 'expediente/signos_vitales/formulario.html'
    success_url = reverse_lazy('expediente:listado_signos_vitales')

class modificarSignoVital(UpdateView):
	model = SignoVital
	form_class = SignoVitalForm
	template_name = 'expediente/signos_vitales/formulario.html'
	success_url = reverse_lazy('expediente:listado_signos_vitales')

def eliminarSignoVital(request, id):
	if not request.is_ajax():
		raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
	signo_vital = SignoVital.objects.get(id = id)
	if request.method == 'GET':
		signo_vital.delete()
		return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Signo Vital de ' + signo_vital.Expediente.Paciente.Persona.nombreCompleto()})
	return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Signo Vital de ' + signo_vital.Expediente.Paciente.Persona.nombreCompleto()})
