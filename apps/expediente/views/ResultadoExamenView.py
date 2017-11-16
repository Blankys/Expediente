from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.ResultadoExamenRequest import ResultadoExamenForm	# desde la carpeta apps/expediente/requests.ResultadoExamenRequest importar la clase ResultadoExamenForm
# ResultadoExamenRequest es un archivo que contiene todos los formularios del area de laboratorio
from apps.expediente.models import ResultadoExamen	# importando modelo
from django.views.generic import ListView, CreateView, TemplateView	# importando clases para las vistas
from django.core.urlresolvers import reverse_lazy	# importando la funcion para redirigir
# Create your views here.

# Nota: {'clave',contexto}: sentencia de un diccionario

'''
def registrarResultadoExamen(request):	# esta funcion permite ingresar los resultados de la evaluacion de laboratorio
	if request.method == 'POST':
		form = ResultadoExamenForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:index')	# redirigiendo a la pagina index. El namespace se encuentra en el archivo urls.py de la carpeta raiz para identificar las vistas correspondientes a la interfaz del area de laboratorio
	else:
		form = ResultadoExamenForm()
	return render(
		request,
		'expediente/examenes/resultados/registrar.html',
		{
			'form': form	# agregando desde la carpeta templates/expediente/registro_respuesta_examen.html y enviando el contexto
		}
	)
'''

# listar
class listadoExamenes(ListView):
	model = ResultadoExamen
	template_name = 'expediente/examenes/resultados/listado.html'	# indicando la plantilla a utilizar

# registro
class respuestaRegistrarResultadoExamen(CreateView):
	model = ResultadoExamen
	form_class = ResultadoExamenForm	# indicando el formulario a utilizar
	template_name = 'expediente/examenes/resultados/registrar.html'	# indicando el tipo de plantilla para el formulario
	# redirigiendo con un url resolver a la vista listar registros de resultado de laboratorio mediante su namespace
	success_url = reverse_lazy('expediente:listado_examenes')

# buscar
class buscarResultadoExamen(TemplateView):
	def post(self, request, *args, **kwargs):
		buscar = request.POST['Busqueda']	# obteniendo el valor del campo de busqueda del formulario contenido en la plantilla listado_registros_resultados_labo.html
		resultadoExamen = ResultadoExamen.objects.filter(Expediente__numeroArchivo = buscar)	# filtrando los datos mediante una FK
		return render(request, 'expediente/examenes/resultados/buscar.html', { 'examenesEncontrados': resultadoExamen })	# enviando los resultados a el template buscar_reg_result_lab.html
