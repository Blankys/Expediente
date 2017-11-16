from django import forms
from apps.expediente.models import Expediente, Paciente, Persona

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