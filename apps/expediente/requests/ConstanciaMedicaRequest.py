from django import forms
from apps.expediente.models import ConstanciaMedica


class ConstanciaForm(forms.ModelForm):

    class Meta:
        model = ConstanciaMedica

        fields = '__all__'

        labels = {
            'dirigidaA':  'Dirigida a',
            'motivoConstancia': 'Motivo de Constancia Medica',
            'fechaEmisionConstancia': 'Fecha de emision',
            'Consulta': 'Consulta',
        }

        widgets = {
            'dirigidaA': forms.TextInput(attrs={'class': 'form-control'}),
            'motivoConstancia': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaEmisionConstancia': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'Consulta': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
        }
