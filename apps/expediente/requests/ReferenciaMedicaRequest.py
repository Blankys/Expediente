from django import forms
from apps.expediente.models import ReferenciaMedica


class ReferenciaMedicaForm(forms.ModelForm):
    class Meta:
        model = ReferenciaMedica

        fields = '__all__'

        labels = {
            'servicioSolicitado': 'Servicio Solicitado',
            'institucionRemitida': 'Institucion Remitida',
            'hallazgosMedicos': 'Hallazgos Medicos',
            'impresionDiagnostica': 'Impresion Diagnostica',
            'doctorReferenciado': 'Doctor Referenciado',
            'motivoReferencia': 'Motivo de Referencia',
            'fechaEmisionRef': 'Fecha de Emision',
            'Consulta': 'Consulta'

        }

        widgets = {
            'servicioSolicitado': forms.TextInput(attrs={'class': 'form-control'}),
            'institucionRemitida': forms.TextInput(attrs={'class': 'form-control'}),
            'hallazgosMedicos': forms.Textarea(attrs={'class': 'form-control'}),
            'impresionDiagnostica': forms.Textarea(attrs={'class': 'form-control'}),
            'doctorReferenciado': forms.Textarea(attrs={'class': 'form-control'}),
            'motivoReferencia': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaEmisionRef': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'Consulta': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'}),
        }
