from django import forms
from apps.expediente.models import IncapacidadMedica


class IncapacidadForm(forms.ModelForm):

    class Meta:
        model = IncapacidadMedica

        fields = '__all__'

        labels = {
        'nombreEmpresa': 'Nombre de la empresa',
        'tipoRiesgo': "Tipo de Riesgo",
        'tipoIncapacidad': 'Tipo de Incapacidad',
        'motivoIncapacidad': 'Motivo de la Incapacidad',
        'diasIncapacidad': 'Dias de Incapacidad',
        'fechaInicioIncapacidad': 'Fecha de Inicio de Incapacidad',
        'fechaFinIncapacidad': 'Fecha de Fin de Incapacidad',
        'fechaEmisionIncapacidad': 'Fecha de Emision de Incapacidad',
        'Consulta': 'Consulta',
    }

        widgets = {
        'nombreEmpresa': forms.TextInput(attrs={'class': 'form-control'}),
        'tipoRiesgo': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        'tipoIncapacidad': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        'motivoIncapacidad': forms.Textarea(attrs={'class': 'form-control'}),
        'diasIncapacidad': forms.NumberInput(attrs = { 'class': 'form-control' }),
        'fechaInicioIncapacidad': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
        'fechaFinIncapacidad': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
        'fechaEmisionIncapacidad': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
        'Consulta': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        }
