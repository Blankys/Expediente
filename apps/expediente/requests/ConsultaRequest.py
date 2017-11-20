from django import forms
from apps.expediente.models import Consulta


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta

        fields = '__all__'

        labels = {
            'fechaConsulta':  'Fecha',
            'motivo': 'Motivo',
            'sintomatologia': 'Sintomas',
            'observaciones': 'Observaciones',
            'diagnostico': 'Diagnostico',
            'fechaProximaConsulta': 'Fecha de Proxima Consulta',
            'Expediente': 'Expediente',
            'CatalogoEnfermedad': 'Tipo de enfermedad',
            'Empleado': 'Doctor',
            'Clinica': 'Clinica'
        }

        widgets = {
            'fechaConsulta': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'motivo': forms.Textarea(attrs={'class': 'form-control'}),
            'sintomatologia': forms.Textarea(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaProximaConsulta': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'Expediente': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'CatalogoEnfermedad': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'Empleado': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'Clinica': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' })
        }
