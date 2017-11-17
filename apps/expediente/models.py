from django.db import models

class CatalogoDepartamento(models.Model):
    nombreDepartamento = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombreDepartamento)

class CatalogoMunicipio(models.Model):
    nombreMunicipio  = models.CharField(max_length = 50)
    CatalogoDepartamento = models.ForeignKey(CatalogoDepartamento, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombreMunicipio)

class Direccion(models.Model):
    detalleDireccion = models.TextField(max_length = 100)
    CatalogoDepartamento = models.ForeignKey(CatalogoDepartamento, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoMunicipio = models.ForeignKey(CatalogoMunicipio, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.detalleDireccion)

class Persona(models.Model):
    primerNombre = models.CharField(max_length = 20)
    segundoNombre = models.CharField(max_length = 20)
    tercerNombre = models.CharField(max_length = 20, null = True, blank = True)
    primerApellido = models.CharField(max_length = 20)
    segundoApellido = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 1, choices = (('F','Femenino'),('M','Masculino')))
    dui = models.CharField(max_length = 10)
    telefonoFijo = models.CharField(max_length = 15, null = True, blank = True)
    telefonoMovil = models.CharField(max_length = 15, null = True, blank = True)
    correoElectronico = models.EmailField(null = True, blank = True)
    Direccion = models.OneToOneField(Direccion, null = False, blank = False, on_delete = models.CASCADE)

    def nombreCompleto(self):
        return '{} {}, {} {}'.format(self.primerNombre, self.segundoNombre, self.primerApellido, self.segundoApellido)

    def __str__(self):
        return '{}'.format(self.nombreCompleto())

class CatalogoTipoClinica(models.Model):
    tipoClinica = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length=50, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.tipoClinica)

class Clinica(models.Model):
    nombre = models.CharField(max_length = 50)
    CatalogoTipoClinica = models.ForeignKey(CatalogoTipoClinica, null = False, blank = False, on_delete = models.CASCADE)
    Direccion = models.OneToOneField(Direccion, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class CatalogoEspecialidadEmpleado(models.Model):
    tipoEspecialidad = models.CharField(max_length = 50)
    descripcionEspecialidad = models.TextField(max_length = 100)

    def __str__(self):
        return '{}'.format(self.tipoEspecialidad)

class Empleado(models.Model):
    fechaIngreso = models.DateField()
    tiempoServicio = models.IntegerField()
    jVPM = models.IntegerField(null = True, blank = True)
    Persona = models.OneToOneField(Persona, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoEspecialidadEmpleado = models.ForeignKey(CatalogoEspecialidadEmpleado, null = True, blank = True, on_delete = models.CASCADE)
    Clinica = models.ForeignKey(Clinica, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Persona)

class Turno(models.Model):
   fechaInicio = models.DateField()
   horaInicio = models.DateTimeField()
   fechaFin = models.DateField()
   horaFin = models.DateTimeField()
   # pendiente de relacionar con auth_user

# Modelos que conforman el expediente del paciente
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

    OCUPACION = (
       ('Empleado Publico', 'Empleado Publico'),
       ('Empleado Privado', 'Empleado Privado'),
       ('Desempleado', 'Desempleado')
    )

    tipoSangre = models.CharField(max_length = 3, choices = SANGRE)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()
    estadoCivil = models.CharField(max_length = 2, choices = ESTADO)
    ocupacion = models.CharField(max_length = 50, choices = OCUPACION)
    Persona = models.OneToOneField(Persona, null = False, blank = False, on_delete = models.CASCADE)
    Clinica = models.ForeignKey(Clinica, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Persona)

class Archivero(models.Model):
    Empleado = models.ForeignKey(Empleado, null = False, blank = False, on_delete = models.CASCADE)
    Clinica = models.ForeignKey(Clinica, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return 'Archivero: {} - Archivista: {}'.format(self.id, self.Empleado)

class CatalogoAlergia(models.Model):
    tipo = models.CharField(max_length = 20)
    reaccion = models.CharField(max_length = 20)
    tratamiento = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.tipo)

class Expediente(models.Model):
    fechaElaboracion = models.DateField()
    Paciente = models.ForeignKey(Paciente, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoAlergia = models.ForeignKey(CatalogoAlergia, null = False, blank = False, on_delete = models.CASCADE)
    Archivero = models.ForeignKey(Archivero, null = False, blank = False, on_delete = models.CASCADE)
    Clinica = models.ForeignKey(Clinica, null = False, blank = False, on_delete = models.CASCADE)

    # Función para mostrar los nombres de los objetos
    def __str__(self):
        return '{}'.format(self.Paciente)

class SignoVital(models.Model):
    presionArterial = models.CharField(max_length = 10)
    frecCardiaca = models.IntegerField()
    frecRespiratoria = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    fechaMedicion = models.DateField()
    notas = models.TextField(max_length = 50, null = True, blank = True)
    Empleado = models.ForeignKey(Empleado, null = False, blank = False, on_delete = models.CASCADE)
    Expediente = models.ForeignKey(Expediente, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Expediente.Paciente)

class ContactoEmergencia(Persona):
    PARENTESCO = (
        ('Padre', 'Padre'),
        ('Madre', 'Madre'),
        ('Hijo', 'Hijo'),
        ('Hermano', 'Hermano'),
        ('Otro', 'Otro')
    )

    relacion = models.CharField(max_length = 20, choices= PARENTESCO)
    Persona = models.OneToOneField(Persona, null = False, blank = False, on_delete = models.CASCADE)
    Expediente = models.ForeignKey(Expediente, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Persona)

class CatalogoEnfermedad(models.Model):
    nombreEnfermedad = models.CharField(max_length = 20)
    descripcionEnfermedad = models.TextField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.nombreEnfermedad)

class AntecedenteFamiliar(models.Model):
    parentesco = models.CharField(max_length = 20)
    CatalogoEnfermedad = models.ForeignKey(CatalogoEnfermedad, null = False, blank = False, on_delete = models.CASCADE)
    Expediente = models.ForeignKey(Expediente, null = False, blank = False, on_delete = models.CASCADE)

# Modelos que conforman la consulta
class Consulta(models.Model):
    fechaConsulta = models.DateField()
    motivo = models.TextField(max_length = 100)
    sintomatologia = models.TextField(max_length = 200)
    observaciones = models.TextField(max_length = 200, null = True, blank = True)
    diagnostico = models.TextField(max_length = 200)
    fechaProximaConsulta = models.DateField(null = True, blank = True)
    Expediente = models.ForeignKey(Expediente, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoEnfermedad = models.ForeignKey(CatalogoEnfermedad, null = False, blank = False, on_delete = models.CASCADE)
    Empleado = models.ForeignKey(Empleado, null = False, blank = False, on_delete = models.CASCADE)
    Clinica = models.ForeignKey(Clinica, null = False, blank = False, on_delete = models.CASCADE)

# Documentos a emitir en una consulta
class ConstanciaMedica(models.Model):
    dirigidaA = models.CharField(max_length = 100)
    motivoConstancia = models.TextField()
    fechaEmisionConstancia = models.DateField()
    Consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)

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

    nombreEmpresa = models.CharField(max_length = 50)
    tipoRiesgo = models.CharField(max_length = 20, choices = RIESGO)
    tipoIncapacidad = models.CharField(max_length = 50, choices = TIPO_INCAPACIDAD)
    motivoIncapacidad = models.TextField()
    diasIncapacidad = models.IntegerField()
    fechaInicioIncapacidad = models.DateField()
    fechaFinIncapacidad = models.DateField()
    fechaEmisionIncapacidad = models.DateField()
    Consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)

class ReferenciaMedica(models.Model):
    servicioSolicitado = models.CharField(max_length = 20)
    institucionRemitida = models.CharField(max_length = 50)
    hallazgosMedicos = models.TextField(null = True, blank = True)
    impresionDiagnostica = models.TextField(null = True, blank = True)
    doctorReferenciado = models.CharField(max_length = 50, null = False, blank = False)
    motivoReferencia = models.TextField(null = True, blank = True)
    fechaEmisionRef = models.DateField()
    Consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)

class RecetaMedica(models.Model):
    fechaEmisionReceta = models.DateField()
    observacionesReceta = models.TextField(max_length = 100, null = True, blank = True)
    Consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)

class CatalogoMedicamento(models.Model):
    nombreMedicamento = models.CharField(max_length = 50)
    modoUso = models.TextField(max_length = 100, null = True, blank = True)
    efectosSecundarios = models.TextField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.nombreMedicamento)

class RecetaMedicamento(models.Model):
    dosis = models.TextField(max_length = 100)
    RecetaMedica = models.ForeignKey(RecetaMedica, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoMedicamento = models.ForeignKey(CatalogoMedicamento, null = False, blank = False, on_delete = models.CASCADE)

# Modelos que conforman un examen médico
class CatalogoTipoExamen(models.Model):
    nombreExamen = models.CharField(max_length = 20)
    descripcionExamen = models.CharField(max_length = 50, null = True, blank = True)
    costo = models.DecimalField(max_digits = 4, decimal_places = 2)

    # Función para mostrar los nombres de los objetos
    def __str__(self):
        return '{}'.format(self.nombreExamen)

class OrdenExamenMedico(models.Model):
    fechaSolicitudExamen = models.DateField()
    estadoOrden = models.CharField(max_length = 10, choices = (('Pendiente','Pendiente'),('Procesando', 'Procesando'),('Finalizado', 'Finalizado')))
    Consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoTipoExamen = models.ForeignKey(CatalogoTipoExamen, null = False, blank = False, on_delete = models.CASCADE)

class ResultadoExamen(models.Model):
    fechaResultado = models.DateField()
    descripcionResultado = models.TextField(max_length = 100, null = True, blank = True)
    Expediente = models.ForeignKey(Expediente, null = False, blank = False, on_delete = models.CASCADE)
    CatalogoTipoExamen = models.ForeignKey(CatalogoTipoExamen, null = False, blank = False, on_delete = models.CASCADE)
    Empleado = models.ForeignKey(Empleado, null = False, blank = False, on_delete = models.CASCADE)

class ArchivoResultadoExamen(models.Model):
    nombreArchivo = models.TextField(max_length=20)
    rutaArchivo = models.TextField(max_length=50)
    descripcionArchivo = models.TextField(max_length=50, null = True, blank= True)
    ResultadoExamen = models.ForeignKey(ResultadoExamen, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombreArchivo)