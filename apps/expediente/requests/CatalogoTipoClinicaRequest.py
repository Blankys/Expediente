from django import forms
from apps.expediente.models import CatalogoTipoClinica


class CatalogoTipoClinicaForm(forms.ModelForm):

    class Meta:
        model = CatalogoTipoClinica

        fields = '__all__'

        labels = {
            'tipoClinica': 'Tipo',
            'descripcion': 'Descripción'
        }

        widgets = {
            'tipoClinica': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }
