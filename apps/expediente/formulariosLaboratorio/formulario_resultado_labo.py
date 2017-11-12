from django import forms
from apps.expediente.models import ResultadoExamen #importando modelo para el formulario

class FormResultLab(forms.ModelForm):

	class Meta:
		model = ResultadoExamen #modelo que servira para el formulario
		
		fields = [
					'fechaResultado',
					'descripcionResultado',
					'Expediente',
					'CatalogoTipoExamen',
					'Empleado',
		]#tupla de campos para mostrar en el formulario

		labels = {

					'fechaResultado':'Fecha de Registro de Resultado de Evaluacion',
					'descripcionResultado':'Descripcion de los Resultados de la Evaluacion',
					'Expediente':'Numero de expediente del paciente',
					'CatalogoTipoExamen':'Tipo de Examen Realizado',
					'Empleado':'Profesional Encargado de Laboratorio',
		}#diccionario de etiquetas que tendran los campos para el formulario

		widgets={
					'fechaResultado':forms.TextInput(),
					'descripcionResultado':forms.TextInput(),
					'Expediente':forms.Select(),
					'CatalogoTipoExamen':forms.Select(),
					'Empleado':forms.Select(),

		}#diccionario comportamiento de los campos del formulario