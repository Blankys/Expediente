from django import forms
from apps.expediente.models import Empleado, Persona

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado

        fields = [
            'fechaIngreso',
            'tiempoServicio',
            'jVPM',
            'CatalogoEspecialidadEmpleado',
            'Clinica'
        ]

        labels = {
            'fechaIngreso': 'Fecha',
            'tiempoServicio': 'Tiempo de Servicio',
            'jVPM': 'JVPM',
            'CatalogoEspecialidadEmpleado': 'Especialidad',
            'Clinica': 'Clinica'
        }

        widgets={
            'fechaIngreso': forms.TextInput(attrs = { 'class': 'form-control fecha', 'placeholder': 'DD/MM/AAAA' }),
            'tiempoServicio': forms.NumberInput(attrs = { 'class': 'form-control' }),
            'jVPM': forms.NumberInput(attrs = { 'class': 'form-control' }),
            'CatalogoEspecialidadEmpleado': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'Clinica': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' })
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = '__all__'

        labels = {
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'tercerNombre': 'Tercer Nombre',
            'primerApellido': 'Primer Apellido',
            'segundoApellido': 'Segundo Apellido',
            'genero': 'Género',
            'dui': 'DUI',
            'telefonoFijo': 'Teléfono Fijo',
            'telefonoMovil': 'Teléfono Movil',
            'correoElectronico': 'Correo Electrónico',
            'Direccion': 'Dirección'
        }

        widgets={
            'primerNombre': forms.TextInput(attrs = { 'class': 'form-control' }),
            'segundoNombre': forms.TextInput(attrs = { 'class': 'form-control' }),
            'tercerNombre': forms.TextInput(attrs = { 'class': 'form-control' }),
            'primerApellido': forms.TextInput(attrs = { 'class': 'form-control' }),
            'segundoApellido': forms.TextInput(attrs = { 'class': 'form-control' }),
            'genero': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'dui': forms.TextInput(attrs = { 'class': 'form-control' }),
            'jVPM': forms.TextInput(attrs = { 'class': 'form-control' }),
            'telefonoFijo': forms.TextInput(attrs = { 'class': 'form-control' }),
            'telefonoMovil': forms.TextInput(attrs = { 'class': 'form-control' }),
            'correoElectronico': forms.EmailInput(attrs = { 'class': 'form-control' }),
            'Direccion': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' })
        }
