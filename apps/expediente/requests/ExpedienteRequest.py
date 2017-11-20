from django import forms
from apps.expediente.models import Expediente, Paciente, Persona, Direccion, ContactoEmergencia

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente

        fields = [
            'fechaElaboracion',
            'CatalogoAlergia',
            'Archivero'
        ]

        labels = {
            'fechaElaboracion' : 'Fecha de Elaboración de Expediente',
            'CatalogoAlergia' : 'Alergias',
            'Archivero': 'Archivero'
        }

        widgets = {
            'fechaElaboracion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'CatalogoAlergia': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10', 'multiple': 'multiple', 'data-actions-box': 'true'}),
            'Archivero': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'})
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = [
            'tipoSangre',
            'fechaNacimiento',
            'edad',
            'estadoCivil',
            'ocupacion'
        ]

        labels = {
            'tipoSangre' : 'Tipo de Sangre',
            'fechaNacimiento' : 'Fecha de Nacimiento',
            'edad' : 'Edad',
            'estadoCivil' : 'Estado Civil',
            'ocupacion' : 'Ocupación',
        }

        widgets = {
            'tipoSangre': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'edad': forms.NumberInput(attrs = { 'class': 'form-control' }),
            'estadoCivil': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' }),
            'ocupacion': forms.Select(attrs = { 'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10' })
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'primerNombre',
            'segundoNombre',
            'tercerNombre',
            'primerApellido',
            'segundoApellido',
            'genero',
            'dui',
            'telefonoFijo',
            'telefonoMovil',
            'correoElectronico'
        ]

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
            'correoElectronico': 'Correo Electrónico'
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
            'correoElectronico': forms.EmailInput(attrs = { 'class': 'form-control' })
        }

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion

        fields = '__all__'

        labels = {
            'detalleDireccion' : 'Dirección',
            'CatalogoMunicipio' : 'Municipio',
            'CatalogoDepartamento' : 'Departamento'
        }

        widgets = {
            'detalleDireccion': forms.Textarea(attrs={'class': 'form-control'}),
            'CatalogoMunicipio': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'}),
            'CatalogoDepartamento': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'})
        }

class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia

        fields = [
            'relacion'
        ]

        labels = {
            'relacion' : 'Parentesco'
        }

        widgets = {
            'relacion': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'})
        }
