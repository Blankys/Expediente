from django import forms
from apps.expediente.models import CatalogoEnfermedad

class CatalogoEnfermedadForm(forms.ModelForm):
	class Meta:
		model = CatalogoEnfermedad

		fields = '__all__'

		labels = {
			'nombreEnfermedad': 'Nombre',
			'descripcionEnfermedad': 'Descripción'
		}

		widgets={
			'nombreEnfermedad': forms.TextInput(attrs = { 'class': 'form-control' }),
			'descripcionEnfermedad': forms.Textarea(attrs = { 'class': 'form-control' })
		}
