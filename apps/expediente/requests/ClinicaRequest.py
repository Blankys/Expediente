from django import forms
from apps.expediente.models import Clinica


class ClinicaForm(forms.ModelForm):

    class Meta:
        model = Clinica

        fields = '__all__'

        labels = {
            'nombre': 'Nombre de Clinica',
            'CatalogoTipoClinica': 'Tipo',
            'Direccion': 'Direccion'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'CatalogoTipoClinica': forms.Select(attrs={'class': 'form-control'}),
            'Direccion': forms.Select(attrs={'class': 'form-control'})
        }
