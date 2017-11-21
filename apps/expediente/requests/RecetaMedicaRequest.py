from django import forms
from apps.expediente.models import RecetaMedica, RecetaMedicamento


class RecetaMedicamentoForm(forms.ModelForm):

    class Meta:
        model = RecetaMedicamento

        fields = '__all__'

        labels = {
        'dosis': 'dosis',
        'RecetaMedica': 'Receta Medica',
        'CatalogoMedicamento': 'Medicamento',
        }

        widgets = {
        'dosis': forms.TextInput(attrs={'class': 'form-control'}),
        'RecetaMedica': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        'CatalogoMedicamento': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
       }

class RecetaMedicaForm(forms.ModelForm):

    class Meta:
        model = RecetaMedica

        fields = '__all__'

        labels = {
        'fechaEmisionReceta': 'Fecha Emision de Receta',
        'observacionesReceta': 'Indicaciones',
        'Consulta': 'Consulta',
        }

        widgets = {
        'fechaEmisionReceta': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
        'observacionesReceta': forms.Textarea(attrs={'class': 'form-control'}),
        'Consulta': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        }
