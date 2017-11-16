from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.expediente.requests.ExamenMedicoRequest import CatalogoTipoExamenForm, OrdenExamenMedicoForm	
# ResultadoExamenRequest es un archivo que contiene todos los formularios del area de laboratorio
from apps.expediente.models import CatalogoTipoExamen, OrdenExamenMedico	# importando modelo
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
		'expediente/examenes/registrar.html',
		{
			'form': form	# agregando desde la carpeta templates/expediente/registro_respuesta_examen.html y enviando el contexto
		}
	)
'''

# listar
class listadoTipoExamen(ListView):
	model = CatalogoTipoExamen
	template_name = 'expediente/examenMedico/listadoTipoExam.html'	# indicando la plantilla a utilizar

# registro
class nuevoTipoExamen(CreateView):
	model = CatalogoTipoExamen 
	form_class = CatalogoTipoExamenForm	# indicando el formulario a utilizar
	template_name = 'expediente/examenMedico/registrarTipoExamen.html'	# indicando el tipo de plantilla para el formulario
	# redirigiendo con un url resolver a la vista listar registros de resultado de laboratorio mediante su namespace
	success_url = reverse_lazy('expediente:listado_tipo_examen')






# listar
class listadoSolicitudExamen(ListView):
	model =  OrdenExamenMedico
	template_name = 'expediente/examennMedico/listOrdenExam.html'	# indicando la plantilla a utilizar
