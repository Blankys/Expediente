from django import forms
from apps.expediente.models import CatalogoEspecialidadEmpleado

class CatalogoEspecialidadEmpleadoForm(forms.ModelForm):
	class Meta:
		model = CatalogoEspecialidadEmpleado

		fields = '__all__'

		labels = {
			'tipoEspecialidad': 'Tipo',
			'descripcionEspecialidad': 'Descripción'
		}

		widgets={
			'tipoEspecialidad': forms.TextInput(attrs = { 'class': 'form-control' }),
			'descripcionEspecialidad': forms.Textarea(attrs = { 'class': 'form-control' })
		}
