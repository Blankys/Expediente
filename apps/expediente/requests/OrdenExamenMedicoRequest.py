from django import forms
from apps.expediente.models import OrdenExamenMedico

class OrdenExamenMedicoForm(forms.ModelForm):
    class Meta:
        model = OrdenExamenMedico

        fields = [
            'fechaSolicitudExamen',
            'estadoOrden',
            'Consulta',
            'CatalogoTipoExamen',
        ]

        labels = {
            'fechaSolicitudExamen': 'Fecha de Examen',
            'estadoOrden': 'Estado de la orden',
            'Consulta': 'Consulta',
            'CatalogoTipoExamen': 'Tipo de Examen'

        }

        widgets = {
            'fechaSolicitudExamen': forms.TextInput(attrs={'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA'}),
            'estadoOrden': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'}),
            'Consulta': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'CatalogoTipoExamen': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'})
        }
