from django import forms
from apps.expediente.models import ArchivoResultadoExamen

class subirResultadosForm(forms.ModelForm):
	class Meta:
		model = ArchivoResultadoExamen

		fields = [
			'nombreArchivo', 
    		'ubicacionArchivo', 
    		'descripcionArchivo', 
    		'fechaRegistro',
    		'ResultadoExamen',
		]

		labels = {
			'nombreArchivo':'Nombre del Archivo', 
    		'ubicacionArchivo':'Seleccionar Archivo', 
    		'descripcionArchivo':'Descripcion del Archivo', 
    		'fechaRegistro':'Fecha de Subida de Archivo',
    		'ResultadoExamen':'Id de Registro de Resultado',	
		}

		widgets = {
			'nombreArchivo': forms.TextInput(attrs = { 'class': 'form-control' }),
			'ubicacionArchivo': forms.FileInput(attrs = { 'class': 'form-control' }),
			'descripcionArchivo': forms.TextInput(attrs = { 'class': 'form-control' }),
			'fechaRegistro': forms.DateInput(attrs = { 'class': 'form-control' }),
			'ResultadoExamen': forms.Select(attrs = { 'class': 'form-control' }),			
		}
