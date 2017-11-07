from django.db import models
# Create your models here.

class CatalogoMunicipio(models.Model):
    idCatalogoMunicipio = models.AutoField (primary_key= True)
    nombreMunicipio  = models.CharField(max_length=50)

class CatalogoDepartamento(models.Model):
    idCatalogoDepartamento = models.AutoField (primary_key= True)
    nombreDepartamento = models.CharField(max_length=50)

class Direccion(models.Model):
    idDireccion = models.AutoField (primary_key= True)
    detalleDireccion = models.TextField(max_length=100)

class Persona(models.Model):
    idPersona = models.AutoField (primary_key= True)
    primerNombre = models.CharField(max_length=20)
    segundoNombre = models.CharField(max_length=20)
    tercerNombre = models.CharField(max_length=20)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    genero = models.CharField(max_length=1, choices=(('F','Femenino'), ('M','Masculino'),))
    dui = models.CharField(max_length=10)
    telefonoFijo = models.CharField(max_length=15)
    telefonoMovil = models.CharField(max_length=15)
    correoElectronico = models.EmailField()

class Empleado(models.Model):
    idEmpleado = models.AutoField (primary_key= True)
    fechaIngreso = models.DateField()
    tiempoServicio = models.IntegerField()
    jVPM = models.IntegerField()

class EspecialidadEmpleado(models.Model):
    idEspecialidadEmpleado = models.AutoField (primary_key= True)
    tipoEspecialidad = models.CharField(max_length=50)
    descripcionEspecialidad = models.TextField(max_length=100)

class Usuario(models.Model):
    idUsuario = models.AutoField (primary_key= True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Turno(models.Model):
   idTurno = models.AutoField (primary_key= True)
   fechaInicio = models.DateField()
   horaInicio = models.DateTimeField()
   fechaFin = models.DateField()
   horaFin = models.DateTimeField()

class Rol(models.Model):
    idRol = models.AutoField (primary_key= True)
    nombreRol = models.CharField(max_length=10)
    
#clases que conforman el expediente del paciente-----
class Paciente(models.Model):
    SANGRE = (
        ('A+', 'Tipo A+'),
        ('B+', 'Tipo B+'),
        ('AB+', 'Tipo AB+'),
        ('O+', 'Tipo O+'),
        ('A-', 'Tipo A-'),
        ('B-', 'Tipo B-'),
        ('AB-', 'Tipo AB-'),
        ('O-', 'Tipo O-'),
    )

    ESTADO= (
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('V', 'Divorciado/a'),
    )

    idPaciente = models.AutoField (primary_key= True)
    tipoSangre = models.CharField(max_length=3, choices=SANGRE)
    fechaNacimiento = models.DateField()
    estadoCivil = models.CharField(max_length=2, choices=ESTADO)
    ocupacion = models.CharField(max_length=50)
    #edad se calcula

class Archivero(models.Model):
    idArchivero = models.AutoField (primary_key= True)
    empleado = models.ForeignKey(Empleado)

class Expediente(models.Model):
    idExpediente = models.AutoField (primary_key= True)
    fechaElaboracion = models.DateField()
    numeroArchivo = models.CharField(max_length=20)
    paciente = models.ForeignKey(Paciente)

class ContactoEmergencia(Persona):
    idContactoEmergencia = models.AutoField (primary_key= True)
    relacion = models.CharField(max_length=20)

class CatalogoAlergia(models.Model):
    idCatalogoAlergia = models.AutoField (primary_key= True)
    tipo = models.CharField(max_length=20)
    reaccion = models.CharField(max_length=20)
    tratamiento = models.CharField(max_length=100)
    expediente = models.ForeignKey(Expediente)

class CatalogoEnfermedad(models.Model):
    idCatalogoEnfermedad = models.AutoField (primary_key= True)
    nombreEnfermedad = models.CharField(max_length=20)
    descripcionEnfermedad = models.TextField(max_length=100)

class SignoVital(models.Model):
    idSignoVital = models.AutoField (primary_key= True)
    presionArterial = models.CharField(max_length=10)
    frecCardiaca = models.IntegerField()
    frecRespiratoria = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    fechaMedicion = models.DateField()
    notas = models.TextField(max_length= 50)
    expediente = models.ForeignKey(Expediente)

class AntecedenteFamiliar(models.Model):
    idAntecedenteFamiliar = models.AutoField (primary_key= True)
    parentesco = models.CharField(max_length=20)
    expediente = models.ForeignKey(Expediente)
    enfermedad = models.ManyToManyField(CatalogoEnfermedad)

#clases que conforman la consulta-----
class Consulta(models.Model):
    idConsulta = models.AutoField (primary_key= True)
    fechaConsulta = models.DateField
    motivo = models.TextField(max_length=100)
    sintomatologia = models.TextField(max_length=200)
    observaciones = models.TextField(max_length=200)
    diagnostico = models.TextField(max_length=200)
    fechaProximaConsulta = models.DateField
    expediente = models.ForeignKey(Expediente)
    enfermedad = models.ManyToManyField(CatalogoEnfermedad)

#documentos a emitir en una consulta (4) -----
class ConstanciaMedica(models.Model):
    idConstanciaMedica = models.AutoField (primary_key= True)
    dirigidaA = models.CharField(max_length=100)
    motivoConstancia = models.TextField()
    fechaEmisionConstancia = models.DateField()
    consulta = models.ForeignKey(Consulta)

class IncapacidadMedica(models.Model):
    RIESGO= (
        ('Enfermedad comun', 'Enfermedad comun'),
        ('Accidente', 'Accidente'),
        ('Maternidad', 'Maternidad'),)

    TIPOINC= (
        ('Inicial', 'Inicial'),
        ('Prorroga', 'Prorroga'),)

    idIncapacidadMedica = models.AutoField (primary_key= True)
    nombreEmpresa = models.CharField(max_length=50)
    tipoRiesgo = models.CharField(max_length=20, choices= RIESGO)
    tipoIncapacidad = models.CharField(max_length=50, choices= TIPOINC)
    motivoIncapacidad = models.TextField()
    diasIncapacidad = models.IntegerField()
    fechaInicioIncapacidad = models.DateField()
    #Fecha fin calculada
    fechaEmisionIncapacidad = models.DateField()
    consulta = models.ForeignKey(Consulta)

class ReferenciaMedica(models.Model):
    idReferenciaMedica = models.AutoField (primary_key= True)
    servicioSolicitado = models.CharField(max_length=20)
    institucionRemitida = models.CharField(max_length=50)
    doctorRemitido = models.CharField(max_length=50)
    hallazgosMedicos = models.TextField()
    impresionDiagnostica = models.TextField()
    motivoReferencia = models.TextField()
    fechaEmisionRef = models.DateField()
    consulta = models.ForeignKey(Consulta)

class RecetaMedica(models.Model):
    idRecetaMedica = models.AutoField (primary_key= True)
    fechaEmisionReceta = models.DateField()
    observacionesReceta = models.TextField(max_length=100)
    consulta = models.ForeignKey(Consulta)
    medicamento = models.ManyToManyField(CatalogoMedicamento, through='RecetaMedicamento')

class RecetaMedicamento(models.Model):
    idRecetaMedicamento = models.AutoField (primary_key= True)
    dosis = models.TextField(max_length=100)
    medicamento = models.ForeignKey(CatalogoMedicamento)
    receta = models.ForeignKey(RecetaMedica)

class CatalogoMedicamento(models.Model):
    idCatalogoMedicamento = models.AutoField (primary_key= True)
    nombreMedicamento = models.CharField(max_length=50)
    modoUso = models.TextField(max_length=100)
    efectosSecundarios = models.TextField(max_length=100)

#clases para generar un examen medico
class OrdenExamenMedico(models.Model):
    idOrdenExamenMedico = models.AutoField (primary_key= True)
    fechaSolicitudExamen= models.DateField()
    estadoOrden= models.CharField(max_length=10, choices=(('Pendiente','Pendiente'), ('Procesando', 'Procesando'), ('Finalizado', 'Finalizado'),))

class CatalogoTipoExamen(models.Model):
    idCatalogoTipoExamen = models.AutoField (primary_key= True)
    nombreExamen= models.CharField(max_length=20)
    descripcionExamen= models.CharField(max_length=50)
    costo = models.FloatField()

class ResultadoExamen(models.Model):
    idResultadoExamen = models.AutoField (primary_key= True)
    fechaResultado= models.DateField()
    descripcionResultado = models.TextField(max_length=100)