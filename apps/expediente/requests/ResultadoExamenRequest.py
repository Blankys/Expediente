from django import forms
from apps.expediente.models import ResultadoExamen

class ResultadoExamenForm(forms.ModelForm):
	class Meta:
		model = ResultadoExamen

		fields = [
			'fechaResultado',
			'descripcionResultado',
			'Expediente',
			'CatalogoTipoExamen',
			'Empleado',
		]

		labels = {
			'fechaResultado': 'Fecha',
			'descripcionResultado': 'Descripción',
			'Expediente': 'Número Expediente',
			'CatalogoTipoExamen': 'Tipo de Examen',
			'Empleado': 'Laboratorista',
		}

		widgets={
			'fechaResultado': forms.DateInput(attrs = { 'class': 'form-control' }),
			'descripcionResultado': forms.TextInput(attrs = { 'class': 'form-control' }),
			'Expediente': forms.Select(attrs = { 'class': 'form-control' }),
			'CatalogoTipoExamen': forms.Select(attrs = { 'class': 'form-control' }),
			'Empleado': forms.Select(attrs = { 'class': 'form-control' }),
		}
