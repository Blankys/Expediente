from django import forms
from apps.expediente.models import CatalogoMedicamento

class CatalogoMedicamentoForm(forms.ModelForm):
	class Meta:
		model = CatalogoMedicamento

		fields = '__all__'

		labels = {
			'nombreMedicamento': 'Nombre',
			'modoUso': 'Modo de Uso',
			'efectosSecundarios': 'Efectos Secundarios'
		}

		widgets={
			'nombreMedicamento': forms.TextInput(attrs = { 'class': 'form-control' }),
			'modoUso': forms.Textarea(attrs = { 'class': 'form-control' }),
			'efectosSecundarios': forms.Textarea(attrs = { 'class': 'form-control' })
		}
