from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.CatalogoEnfermedadRequest import CatalogoEnfermedadForm
from apps.expediente.models import CatalogoEnfermedad

class listadoEnfermedades(ListView):
    model = CatalogoEnfermedad
    template_name = 'expediente/enfermedades/listado.html'

class agregarEnfermedad(CreateView):
    model = CatalogoEnfermedad
    form_class = CatalogoEnfermedadForm
    template_name = 'expediente/enfermedades/formulario.html'
    success_url = reverse_lazy('expediente:listado_enfermedades')

class modificarEnfermedad(UpdateView):
	model = CatalogoEnfermedad
	form_class = CatalogoEnfermedadForm
	template_name = 'expediente/enfermedades/formulario.html'
	success_url = reverse_lazy('expediente:listado_enfermedades')

def eliminarEnfermedad(request, id):
	if not request.is_ajax():
		raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
	enfermedad = CatalogoEnfermedad.objects.get(id = id)
	if request.method == 'GET':
		enfermedad.delete()
		return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Enfermedad ' + enfermedad.nombreEnfermedad})
	return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Enfermedad ' + enfermedad.nombreEnfermedad})
