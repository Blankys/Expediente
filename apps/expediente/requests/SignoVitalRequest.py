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
			'presionArterial': 'Presion Arterial',
			'frecCardiaca': 'Frecuencia Cardiaca',
			'frecRespiratoria': 'Frecuencia Respiratoria',
			'peso': 'Peso',
			'altura': 'Altura',
			'fechaMedicion': 'Fecha',
			'notas': 'Notas',
			'Empleado': 'Enfermera'
		}

		widgets={
			'presionArterial': forms.TextInput(),
			'frecCardiaca': forms.TextInput(),
			'frecRespiratoria': forms.TextInput(),
			'peso': forms.NumberInput(),
			'altura': forms.NumberInput(),
			'fechaMedicion': forms.SelectDateWidget(),
			'notas': forms.Textarea(),
			'Empleado': forms.Select(),
		}
