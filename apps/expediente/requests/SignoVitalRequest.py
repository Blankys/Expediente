from django import forms
from apps.expediente.models import SignoVital

class SignoVitalForm(forms.ModelForm):
	class Meta:
		model = SignoVital

		fields = [
			'presionArterial',
			'frecCardiaca',
			'frecRespiratoria',
			'peso',
			'altura',
			'fechaMedicion',
			'notas',
			'Empleado'
		]

		labels = {
			'presionArterial': 'Presión Arterial',
			'frecCardiaca': 'Frecuencia Cardíaca',
			'frecRespiratoria': 'Frecuencia Respiratoria',
			'peso': 'Peso',
			'altura': 'Altura',
			'fechaMedicion': 'Fecha',
			'notas': 'Notas',
			'Empleado': 'Enfermera'
		}

		widgets={
			'presionArterial': forms.TextInput(attrs = { 'class': 'form-control' }),
			'frecCardiaca': forms.TextInput(attrs = { 'class': 'form-control' }),
			'frecRespiratoria': forms.TextInput(attrs = { 'class': 'form-control' }),
			'peso': forms.NumberInput(attrs = { 'class': 'form-control' }),
			'altura': forms.NumberInput(attrs = { 'class': 'form-control' }),
			'fechaMedicion': forms.DateInput(attrs = { 'class': 'form-control' }),
			'notas': forms.Textarea(attrs = { 'class': 'form-control' }),
			'Empleado': forms.Select(attrs = { 'class': 'form-control' }),
		}
