from django import forms
from apps.expediente.models import Turno


class TurnoForm(forms.ModelForm):

    class Meta:
        model = Turno

        fields = '__all__'

        labels = {
            'fechaInicio': 'Fecha de Inicio',
            'horaInicio': 'Hora de Inicio',
            'fechaFin': 'Fecha de Fin',
            'horaFin': 'Hora de Fin',
            'Empleado': 'Empleado'
        }

        widgets = {
            'fechaInicio': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'horaInicio': forms.TextInput(attrs = { 'class': 'form-control hora', 'placeholder': 'HH/MM/SS' }),
            'fechaFin': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'horaFin': forms.TextInput(attrs = { 'class': 'form-control hora', 'placeholder': 'HH/MM/SS' }),
            'Empleado': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' })
        }
