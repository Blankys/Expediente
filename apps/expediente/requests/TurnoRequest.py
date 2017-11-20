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
            'horaFin': 'Hora de Fin'
        }

        widgets = {
            'fechaInicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'horaInicio': forms.TimeInput(attrs={'class': 'form-control'}),
            'fechaFin': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'horaFin': forms.TimeInput(attrs={'class': 'form-control'}),
        }
