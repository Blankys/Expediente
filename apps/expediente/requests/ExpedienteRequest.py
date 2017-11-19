from django import forms
from apps.expediente.models import Expediente, Paciente, Persona, Direccion, ContactoEmergencia

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente

        fields = "__all__"

        labels = {
            'fechaElaboracion' : 'Fecha de Elaboración',
            'CatalogoAlergia' : 'Alergia',
        }

        widgets = {
            'CatalogoAlergia': forms.CheckboxSelectMultiple(),
            'Paciente' : forms.HiddenInput(),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = '__all__'

        labels = {
            'tipoSangre' : 'Tipo de Sangre',
            'fechaNacimiento' : 'Fecha de Nacimiento (DD/MM/AAAA)',
            'edad' : 'Edad',
            'estadoCivil' : 'Estado Civil',
            'ocupacion' : 'Ocupación',
        }

        widgets = {
            'Persona': forms.HiddenInput(),
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = '__all__'

        labels = {
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'tercerNombre' : 'Tercer Nombre',
            'primerApellido' : 'Primer Apellido',
            'segundoApellido' : 'Segundo Apellido',
            'genero' : 'Género',
            'dui' : 'DUI',
            'telefonoFijo' : 'Teléfono Fijo',
            'telefonoMovil' : 'Teléfono Movil',
            'correoElectronico' : 'Correo Electrónico'
        }

        widgets = {
            'Direccion': forms.HiddenInput
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

class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia

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
            'relacion' : 'Parentesco'
        }

        widgets = {
            'Persona' : forms.HiddenInput,
            'Expediente' : forms.HiddenInput,
            'Direccion' : forms.HiddenInput
        }