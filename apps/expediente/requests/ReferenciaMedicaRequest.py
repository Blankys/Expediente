from django import forms
from apps.expediente.models import ReferenciaMedica


class ReferenciaMedicaForm(forms.ModelForm):
    class Meta:
        model = ReferenciaMedica

        fields = [
            'institucionRemitida',
            'hallazgosMedicos',
            'impresionDiagnostica',
            'doctorReferenciado',
            'motivoReferencia',
            'fechaEmisionRef',

        ]

        labels = {
            'institucionRemitida': 'Institucion Remitida',
            'hallazgosMedicos': 'Hallazgos Medicos',
            'impresionDiagnostica': 'Impresion Diagnostica',
            'doctorReferenciado': 'Doctor Referenciado',
            'motivoReferencia': 'Motivo de Referencia',
            'fechaEmisionRef': 'Fecha de Emision',


        }

        widgets = {
            'institucionRemitida': forms.Textarea(attrs={'class': 'form-control'}),
            'hallazgosMedicos': forms.Textarea(attrs={'class': 'form-control'}),
            'impresionDiagnostica': forms.Textarea(attrs={'class': 'form-control'}),
            'doctorReferenciado': forms.Textarea(attrs={'class': 'form-control'}),
            'motivoReferencia': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaEmisionRef': forms.DateInput(attrs={'class': 'form-control'}),

        }
