from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.expediente.formulariosLaboratorio.formulario_resultado_labo import FormResultLab #desde la carpeta apps/expediente/formulariosLaboratorio.formulario_resultado_labo importar la clase FormResultLab
#formulariosLaboratorio es una carpeta que contiene todos los formularios del area de laboratorio
from apps.expediente.models import ResultadoExamen #importando modelo

# Create your views here.
# {'clave',contexto}: sentencia de un diccionario
def index(request):
	#return HttpResponse("index")
	return render(request,'expediente/registro_respuesta_examen.html')

def ver_form_registro_result_labo(request):# esta funcion permite ingresar los resultados de la evaluacion de laboratorio
	if request.method == 'POST':
		form = FormResultLab(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:index')#redirigiendo a la pagina index. El namespace se encuentra en el archivo urls.py de la carpeta raiz para identificar las vistas correspondientes a la interfaz del area de laboratorio
	else: 
		form = FormResultLab()
	return render(request, 'expediente/registro_respuesta_examen.html',{'form':form})# agregando desde la carpeta templates/expediente/registro_respuesta_examen.html y enviando el contexto


def ver_listado_reg_result_lab(request):
	listado = ResultadoExamen.objects.all() #QuerySet para traer todos los objetos que se encuentran en el modelo de ResultadoExamen
	#enviando contexto
	contexto = {'list_reg_result_lab':listado} # la variable contexto contiene el diccionario que contiene el listado de los objetos del modelo ResultadoExamen
	return render(request,'expediente/listado_registros_resultados_labo.html',contexto)#enviando el contexto a la plantilla ver_listado_reg_result_lab.html localizada en la carpeta expediente de las templates
