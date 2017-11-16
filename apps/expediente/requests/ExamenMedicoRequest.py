from django import forms
from apps.expediente.models import CatalogoTipoExamen, OrdenExamenMedico

class CatalogoTipoExamenForm(forms.ModelForm):
	class Meta:
		model = CatalogoTipoExamen

		fields = [
			'nombreExamen',
			'descripcionExamen',
			'costo',
			
		]

		labels = {
			'nombreExamen': 'Nombre examen',
			'descripcionExamen': 'Descripción examen',
			'costo': 'Costo examen',
			
		}

		widgets={
			'nombreExamen': forms.TextInput(attrs = { 'class': 'form-control' }),
			'descripcionExamen': forms.Textarea(attrs = { 'class': 'form-control' }),
			'costo': forms.TextInput(attrs = { 'class': 'form-control' }),
			
		}



class OrdenExamenMedicoForm(forms.ModelForm):
	class Meta:
		model = OrdenExamenMedico

		fields = [
			'fechaSolicitudExamen',
			'estadoOrden',
			'Consulta',
			'CatalogoTipoExamen',
		]

		labels = {
			'fechaSolicitudExamen': 'Fecha examen',
			'estadoOrden': 'Estado orden',
			'Consulta': 'Consulta',
			'CatalogoTipoExamen': 'Catalogo tipoExam'
			
		}

		widgets={
			'fechaSolicitudExamen': forms.DateInput(attrs = { 'class': 'form-control' }),
			'estadoOrden': forms.TextInput(attrs = { 'class': 'form-control' }),
			'Consulta': forms.TextInput(attrs = { 'class': 'form-control' }),
			'CatalogoTipoExamen': forms.Select(attrs = { 'class': 'form-control' }),
			
		}





