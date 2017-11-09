from django.db import models

class CatalogoDepartamento(models.Model):
    idCatalogoDepartamento = models.AutoField(primary_key = True, unique = True)
    nombreDepartamento = models.CharField(max_length = 50)

class CatalogoMunicipio(models.Model):
    idCatalogoMunicipio = models.AutoField(primary_key = True, unique = True)
    nombreMunicipio  = models.CharField(max_length = 50)
    departamento = models.ForeignKey(CatalogoDepartamento, to_field = 'idCatalogoDepartamento', null = False, blank = False, on_delete = models.CASCADE)

class Persona(models.Model):
    idPersona = models.AutoField(primary_key = True, unique = True)
    primerNombre = models.CharField(max_length = 20)
    segundoNombre = models.CharField(max_length = 20)
    tercerNombre = models.CharField(max_length = 20)
    primerApellido = models.CharField(max_length = 20)
    segundoApellido = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 1, choices = (('F','Femenino'),('M','Masculino')))
    dui = models.CharField(max_length = 10)
    telefonoFijo = models.CharField(max_length = 15)
    telefonoMovil = models.CharField(max_length = 15)
    correoElectronico = models.EmailField()

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key = True, unique = True)
    detalleDireccion = models.TextField(max_length = 100)
    persona = models.OneToOneField(Persona, to_field = 'idPersona', null = False, blank = False, on_delete = models.CASCADE)
    departamento = models.ForeignKey(CatalogoDepartamento, to_field = 'idCatalogoDepartamento', null = False, blank = False, on_delete = models.CASCADE)
    municipio = models.ForeignKey(CatalogoMunicipio, to_field = 'idCatalogoMunicipio', null = False, blank = False, on_delete = models.CASCADE)

class EspecialidadEmpleado(models.Model):
    idEspecialidadEmpleado = models.AutoField(primary_key = True, unique = True)
    tipoEspecialidad = models.CharField(max_length = 50)
    descripcionEspecialidad = models.TextField(max_length = 100)

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key = True, unique = True)
    fechaIngreso = models.DateField()
    tiempoServicio = models.IntegerField()
    jVPM = models.IntegerField()
    persona = models.OneToOneField(Persona, to_field = 'idPersona', null = False, blank = False, on_delete = models.CASCADE)
    especialidadEmpleado = models.ForeignKey(EspecialidadEmpleado, to_field = 'idEspecialidadEmpleado', null = True, blank = True, on_delete = models.CASCADE)

class Rol(models.Model):
    idRol = models.AutoField(primary_key = True, unique = True)
    nombreRol = models.CharField(max_length = 10)

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, unique = True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    empleado = models.OneToOneField(Empleado, to_field = 'idEmpleado', null = False, blank = False, on_delete = models.CASCADE)
    rol = models.ForeignKey(Rol, to_field = 'idRol', null = False, blank = False, on_delete = models.CASCADE)

class Turno(models.Model):
   idTurno = models.AutoField(primary_key = True, unique = True)
   fechaInicio = models.DateField()
   horaInicio = models.DateTimeField()
   fechaFin = models.DateField()
   horaFin = models.DateTimeField()
   usuario = models.ForeignKey(Usuario, to_field = 'idUsuario', null = False, blank = False, on_delete = models.CASCADE)

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

    ESTADO = (
       ('S', 'Soltero/a'),
       ('C', 'Casado/a'),
       ('V', 'Divorciado/a'),
    )

    idPaciente = models.AutoField(primary_key = True, unique = True)
    tipoSangre = models.CharField(max_length = 3, choices = SANGRE)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()
    estadoCivil = models.CharField(max_length = 2, choices = ESTADO)
    ocupacion = models.CharField(max_length = 50)
    persona = models.OneToOneField(Persona, to_field = 'idPersona', null = False, blank = False, on_delete = models.CASCADE)

class Archivero(models.Model):
    idArchivero = models.AutoField(primary_key = True, unique = True)
    archivista = models.ForeignKey(Empleado, to_field = 'idEmpleado', null = False, blank = False, on_delete = models.CASCADE)

class CatalogoAlergia(models.Model):
    idCatalogoAlergia = models.AutoField(primary_key = True, unique = True)
    tipo = models.CharField(max_length = 20)
    reaccion = models.CharField(max_length = 20)
    tratamiento = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 100)

class SignoVital(models.Model):
    idSignoVital = models.AutoField(primary_key = True, unique = True)
    presionArterial = models.CharField(max_length = 10)
    frecCardiaca = models.IntegerField()
    frecRespiratoria = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    fechaMedicion = models.DateField()
    notas = models.TextField(max_length = 50)
    enfermera = models.ForeignKey(Empleado, to_field = 'idEmpleado', null = False, blank = False, on_delete = models.CASCADE)

class Expediente(models.Model):
    idExpediente = models.AutoField(primary_key = True, unique = True)
    fechaElaboracion = models.DateField()
    numeroArchivo = models.CharField(max_length = 20)
    paciente = models.ForeignKey(Paciente, to_field = 'idPaciente', null = False, blank = False, on_delete = models.CASCADE)
    alergia = models.ForeignKey(CatalogoAlergia, to_field = 'idCatalogoAlergia', null = False, blank = False, on_delete = models.CASCADE)
    signoVital = models.ForeignKey(SignoVital, to_field = 'idSignoVital', null = False, blank = False, on_delete = models.CASCADE)
    archivero = models.ForeignKey(Archivero, to_field = 'idArchivero', null = False, blank = False, on_delete = models.CASCADE)

class ContactoEmergencia(Persona):
    idContactoEmergencia = models.AutoField(primary_key = True, unique = True)
    relacion = models.CharField(max_length = 20)
    persona = models.OneToOneField(Persona, to_field = 'idPersona', null = False, blank = False, on_delete = models.CASCADE)
    expediente = models.ForeignKey(Expediente, to_field='idExpediente', null=False, blank=False, on_delete=models.CASCADE)

class CatalogoEnfermedad(models.Model):
    idCatalogoEnfermedad = models.AutoField(primary_key = True, unique = True)
    nombreEnfermedad = models.CharField(max_length = 20)
    descripcionEnfermedad = models.TextField(max_length = 100)

class AntecedenteFamiliar(models.Model):
    idAntecedenteFamiliar = models.AutoField(primary_key = True, unique = True)
    parentesco = models.CharField(max_length = 20)
    enfermedad = models.ForeignKey(CatalogoEnfermedad, to_field = 'idCatalogoEnfermedad', null = False, blank = False, on_delete = models.CASCADE)
    expediente = models.ForeignKey(Expediente, to_field = 'idExpediente', null = False, blank = False, on_delete = models.CASCADE)

#clases que conforman la consulta-----
class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key = True, unique = True)
    fechaConsulta = models.DateField
    motivo = models.TextField(max_length = 100)
    sintomatologia = models.TextField(max_length = 200)
    observaciones = models.TextField(max_length = 200)
    diagnostico = models.TextField(max_length = 200)
    fechaProximaConsulta = models.DateField
    expediente = models.ForeignKey(Expediente, to_field = 'idExpediente', null = False, blank = False, on_delete = models.CASCADE)
    enfermedad = models.ForeignKey(CatalogoEnfermedad, to_field = 'idCatalogoEnfermedad', null = False, blank = False, on_delete = models.CASCADE)
    medico = models.ForeignKey(Empleado, to_field = 'idEmpleado', null = False, blank = False, on_delete = models.CASCADE)

#documentos a emitir en una consulta(4) -----
class ConstanciaMedica(models.Model):
    idConstanciaMedica = models.AutoField(primary_key = True, unique = True)
    dirigidaA = models.CharField(max_length = 100)
    motivoConstancia = models.TextField()
    fechaEmisionConstancia = models.DateField()
    consulta = models.ForeignKey(Consulta, to_field = 'idConsulta', null = False, blank = False, on_delete = models.CASCADE)

class IncapacidadMedica(models.Model):
    RIESGO = (
       ('Enfermedad comun', 'Enfermedad comun'),
       ('Accidente', 'Accidente'),
       ('Maternidad', 'Maternidad')
    )

    TIPO_INCAPACIDAD = (
       ('Inicial', 'Inicial'),
       ('Prorroga', 'Prorroga')
    )

    idIncapacidadMedica = models.AutoField(primary_key = True, unique = True)
    nombreEmpresa = models.CharField(max_length = 50)
    tipoRiesgo = models.CharField(max_length = 20, choices = RIESGO)
    tipoIncapacidad = models.CharField(max_length = 50, choices = TIPO_INCAPACIDAD)
    motivoIncapacidad = models.TextField()
    diasIncapacidad = models.IntegerField()
    fechaInicioIncapacidad = models.DateField()
    fechaFinIncapacidad = models.DateField()
    fechaEmisionIncapacidad = models.DateField()
    consulta = models.ForeignKey(Consulta, to_field = 'idConsulta', null = False, blank = False, on_delete = models.CASCADE)

class ReferenciaMedica(models.Model):
    idReferenciaMedica = models.AutoField(primary_key = True, unique = True)
    servicioSolicitado = models.CharField(max_length = 20)
    institucionRemitida = models.CharField(max_length = 50)
    hallazgosMedicos = models.TextField()
    impresionDiagnostica = models.TextField()
    doctorReferenciado = models.CharField(max_length = 50, null = False, blank = False)
    motivoReferencia = models.TextField()
    fechaEmisionRef = models.DateField()
    consulta = models.ForeignKey(Consulta, to_field = 'idConsulta', null = False, blank = False, on_delete = models.CASCADE)

class RecetaMedica(models.Model):
    idRecetaMedica = models.AutoField(primary_key = True, unique = True)
    fechaEmisionReceta = models.DateField()
    observacionesReceta = models.TextField(max_length = 100)
    consulta = models.ForeignKey(Consulta, to_field = 'idConsulta', null = False, blank = False, on_delete = models.CASCADE)

class CatalogoMedicamento(models.Model):
    idCatalogoMedicamento = models.AutoField(primary_key = True, unique = True)
    nombreMedicamento = models.CharField(max_length = 50)
    modoUso = models.TextField(max_length = 100)
    efectosSecundarios = models.TextField(max_length = 100)

class RecetaMedicamento(models.Model):
    idRecetaMedicamento = models.AutoField(primary_key = True, unique = True)
    dosis = models.TextField(max_length = 100)
    receta = models.ForeignKey(RecetaMedica, to_field = 'idRecetaMedica', null = False, blank = False, on_delete = models.CASCADE)
    medicamento = models.ForeignKey(CatalogoMedicamento, to_field = 'idCatalogoMedicamento', null = False, blank = False, on_delete = models.CASCADE)

#clases para generar un examen medico
class CatalogoTipoExamen(models.Model):
    idCatalogoTipoExamen = models.AutoField(primary_key = True, unique = True)
    nombreExamen = models.CharField(max_length = 20)
    descripcionExamen = models.CharField(max_length = 50)
    costo = models.DecimalField(max_digits = 4, decimal_places = 2)

class OrdenExamenMedico(models.Model):
    idOrdenExamenMedico = models.AutoField(primary_key = True, unique = True)
    fechaSolicitudExamen = models.DateField()
    estadoOrden = models.CharField(max_length = 10, choices = (('Pendiente','Pendiente'),('Procesando', 'Procesando'),('Finalizado', 'Finalizado')))
    consulta = models.ForeignKey(Consulta, to_field = 'idConsulta', null = False, blank = False, on_delete = models.CASCADE)
    examen = models.ForeignKey(CatalogoTipoExamen, to_field = 'idCatalogoTipoExamen', null = False, blank = False, on_delete = models.CASCADE)

class ResultadoExamen(models.Model):
    idResultadoExamen = models.AutoField(primary_key = True, unique = True)
    fechaResultado = models.DateField()
    descripcionResultado = models.TextField(max_length = 100)
    expediente = models.ForeignKey(Expediente, to_field = 'idExpediente', null = False, blank = False, on_delete = models.CASCADE)
    examen = models.ForeignKey(CatalogoTipoExamen, to_field = 'idCatalogoTipoExamen', null = False, blank = False, on_delete = models.CASCADE)
    laboratorista = models.ForeignKey(Empleado, to_field = 'idEmpleado', null = False, blank = False, on_delete = models.CASCADE)
