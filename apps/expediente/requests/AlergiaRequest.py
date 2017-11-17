
from django import forms # se importan los forms de django
from apps.expediente.models import CatalogoAlergia



class AlergiaForm(forms.ModelForm): #se crea una clase MascotaForm que hereda de ModelsForm

	class Meta: #se crea para indicarle partiendo de que modelo se va a crear el formulario en este caso se parte del modelo Persona
		model = CatalogoAlergia
		#se crean 3 tuplas
		fields = [

			'tipo',
			'reaccion',
			'tratamiento',
			'descripcion',

		]
		labels = {
			'tipo': 'Tipo',
			'reaccion': 'Reaccion ',
			'tratamiento': 'Tratamiento',
			'descripcion': 'Descripcion',


		}
		widgets = { #estos apareceran en forma de etiquetas html, el primer dato es el atributo definido en el modelo...EL CODiGO DE LAS LLAVES FORANEAS SUJETAS A CAMBIO
			'tipo': forms.TextInput(attrs={'class':'form-control'}),
			'reaccion': forms.TextInput(attrs={'class':'form-control'}),
			'tratamiento': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),



		}




