from django.db import models

# Create your models here.

class CatalogoMunicipio(models.Model):
    nombreMunicipio  = models.CharField(max_length=50)
    departamento = models.CharField(max_length=2, choices=(('AH','Ahuachapán'), ('CA','Cabañas'),
                                                                 ('CH', 'Chalatenango'), ('CU','Cuscatlán'),
                                                                 ('LI', 'La Libertad'), ('MO', 'Morazán'),
                                                                 ('PA', 'La Paz'), ('SA', 'Santa Ana'),
                                                                 ('SM', 'San Miguel'), ('SO', 'Sonsonate'),
                                                                 ('SS', 'San Salvador'), ('SV', 'San Vicente'),
                                                                 ('UN', 'La Unión'), ('US', 'Usulután'),))


class Persona(models.Model):
    primerNombre = models.CharField(max_length=20)
    segundoNombre = models.CharField(max_length=20)
    tercerNombre = models.CharField(max_length=20)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    dui = models.CharField(max_length=10)
    telefonoFijo = models.CharField(max_length=15)
    telefonoMovil = models.CharField(max_length=15)
    correo = models.EmailField()

class Direccion(models.Model):
    detalle = models.CharField(max_length=100)
    municipio = models.ForeignKey(CatalogoMunicipio)
    persona = models.ForeignKey(Persona)

class ContactoEmergencia(Persona):
    relacion = models.CharField(max_length=20)

class Paciente(Persona):
    tipoSangre = models.CharField(max_length=2)
    fechaNac = models.DateField()
    estadoCivil = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=50)
    contactoEmergencia = models.ForeignKey(ContactoEmergencia, null=True, blank=True)

class Expediente(models.Model):
    fechaElaboracion = models.DateField()
    numeroArchivo = models.CharField(max_length=20)
    paciente = models.ForeignKey(Paciente)

class CatalogoEnfermedad(models.Model):
    nombreEnfermedad = models.CharField(max_length=20)
    descripcionEnfermedad = models.TextField(max_length=100)

class Consulta(models.Model):
    fechaConsulta = models.DateField
    motivo = models.TextField(max_length=100)
    sintomatologia = models.TextField(max_length=200)
    observaciones = models.TextField(max_length=200)
    diagnostico = models.TextField(max_length=200)
    fechaProxConsulta = models.DateField
    expediente = models.ForeignKey(Expediente)
    enfermedad = models.ManyToManyField(CatalogoEnfermedad)

class SignosVitales(models.Model):
    presionArterial = models.CharField(max_length=10)
    frecCardiaca = models.IntegerField()
    frecRespiratoria = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    fechaMedicion = models.DateField()
    expediente = models.ForeignKey(Expediente)

class Alergia(models.Model):
    tipo = models.CharField(max_length=20)
    reaccion = models.CharField(max_length=20)
    tratamiento = models.CharField(max_length=100)
    descripcion = models.TextField()
    expediente = models.ForeignKey(Expediente)

class AntecedenteFamiliare(models.Model):
    parentesco = models.CharField(max_length=20)
    expediente = models.ForeignKey(Expediente)
    enfermedad = models.ManyToManyField(CatalogoEnfermedad)


class CatalogoMedicamento(models.Model):
    nombreMedicamento = models.CharField(max_length=50)
    dosisMedicamento = models.CharField(max_length=20)
    modoUso = models.TextField(max_length=100)
    efectosSecundarios = models.TextField(max_length=100)

class RecetaMedica(models.Model):
    fechaEmision = models.DateField()
    observacionesReceta = models.TextField(max_length=100)
    consulta = models.ForeignKey(Consulta)
    medicamento = models.ManyToManyField(CatalogoMedicamento, through='RecetaMedicamento')


class RecetaMedicamento(models.Model):
    dosis = models.TextField(max_length=100)
    medicamento = models.ForeignKey(CatalogoMedicamento)
    receta = models.ForeignKey(RecetaMedica)


class ConstanciaMedica(models.Model):
    dirigidaA = models.CharField(max_length=100)
    motivoConstancia = models.TextField()
    fechaEmisionConst = models.DateField()
    consulta = models.ForeignKey(Consulta)

class ReferenciaMedica(models.Model):
    servicioSolicitado = models.CharField(max_length=20)
    institucionRemitida = models.CharField(max_length=50)
    hallazgosMedicos = models.TextField()
    impresionDiagnostica = models.TextField()
    motivoReferencia = models.TextField()
    fechaEmisionRef = models.DateField()
    consulta = models.ForeignKey(Consulta)

class IncapacidadMedica(models.Model):
    nomEmpresa = models.CharField(max_length=50)
    tipoRiesgo = models.CharField(max_length=20)
    tipoIncapacidad = models.CharField(max_length=50)
    motivoIncapacidad = models.TextField()
    diasIncapacidad = models.IntegerField()
    fechaInicio = models.DateField()
    #Fecha fin calculada
    fechaEmision = models.DateField()
    consulta = models.ForeignKey(Consulta)