from django.conf.urls import url
from apps.expediente.views.GeneralView import index, municipios
from apps.expediente.views.ResultadoExamenView import respuestaRegistrarResultadoExamen, listadoExamenes, buscarResultadoExamen,uploadResultadosEscaneados,actualizarRegResultExam,listadoArchivoResultados
from apps.expediente.views.SignoVitalView import ListadoSignosVitales, AgregarSignoVital, ModificarSignoVital, eliminarSignoVital
from apps.expediente.views.ReferenciaMedicaView import registrarReferenciaMedica, listadoReferenciaMedica
from apps.expediente.views.ExpedienteView import agregarExpediente, listadoExpedientes, modificarExpediente, eliminarExpediente
from apps.expediente.views.ExamenMedicoView import listadoTipoExamen, listadoSolicitudExamen, nuevoTipoExamen
from apps.expediente.views.AlergiaView import AlergiaCreate, AlergiaList, AlergiaUpdate
from apps.expediente.views.CatalogoEnfermedadView import ListadoEnfermedades, AgregarEnfermedad, ModificarEnfermedad, eliminarEnfermedad
from apps.expediente.views.CatalogoEspecialidadEmpleadoView import ListadoEspecialidadesEmpleados, AgregarEspecialidadEmpleado, ModificarEspecialidadEmpleado, eliminarEspecialidadEmpleado
from apps.expediente.views.CatalogoMedicamentoView import ListadoMedicamentos, AgregarMedicamento, ModificarMedicamento, eliminarMedicamento
from apps.expediente.views.EmpleadoView import ListadoEmpleados, AgregarEmpleado, ModificarEmpleado, eliminarEmpleado
from apps.expediente.views.CatalogoTipoClinicaView import ListadoTipoClinicas, AgregarTipoClinica, ModificarTipoClinica, eliminarTipoClinica
from apps.expediente.views.ClinicaView import ListadoClinica, AgregarClinica, ModificarClinica, eliminarClinica
from apps.expediente.views.ConsultaView import ListadoConsultas, RegistrarConsulta, ModificarConsulta, eliminarConsulta
from apps.expediente.views.TurnoView import ListadoTurnos, AgregarTurno, ModificarTurno, eliminarTurno

urlpatterns = [
    # General
    url(r'^$', index, name = 'inicio'),
    url(r'^ajax/municipios/$', municipios, name = 'ajax_municipios'),

    # ResultadoExamen
    url(r'^examenes/resultados/registrar$', respuestaRegistrarResultadoExamen.as_view(), name = 'registrar_resultado_examen'),
    url(r'^examenes/resultados/listado$', listadoExamenes.as_view(), name = 'listado_examenes'),
    url(r'^examenes/resultados/buscar$', buscarResultadoExamen.as_view(template_name = 'expediente/examenes/buscar.html'), name = 'buscar_examen'),
    url(r'^examenes/resultados/subir$', uploadResultadosEscaneados.as_view(), name='resultados_escaneados'),
     url(r'^examenes/resultados/modificar/(?P<pk>\d+)$', actualizarRegResultExam.as_view(), name = 'modificar_examen'),
     url(r'^examenes/resultados/listado_archivos$', listadoArchivoResultados.as_view(), name = 'listado_archivos'),

    # SignoVital
    url(r'^signos-vitales/agregar$', AgregarSignoVital.as_view(), name = 'agregar_signo_vital'),
    url(r'^signos-vitales/listado$', ListadoSignosVitales.as_view(), name = 'listado_signos_vitales'),
    url(r'^signos-vitales/modificar/(?P<pk>\d+)/$', ModificarSignoVital.as_view(), name = 'modificar_signo_vital'),
    url(r'^signos-vitales/eliminar/(?P<id>\d+)/$', eliminarSignoVital, name = 'eliminar_signo_vital'),

    # ReferenciaMedica
    url(r'^referencias/listado$',listadoReferenciaMedica, name = 'listado_referencia_medica'),
    url(r'^referencias/registrar$',registrarReferenciaMedica, name = 'registrar_referencia_medica'),

    # Expediente
    url(r'^expedientes/agregar$', agregarExpediente, name = 'agregar_expediente'),
    url(r'^expedientes/listado$', listadoExpedientes.as_view(), name = 'listado_expedientes'),
    url(r'^expedientes/modificar/(?P<id>\d+)/$', modificarExpediente, name = 'modificar_expediente'),
    url(r'^expedientes/eliminar/(?P<id>\d+)/$', eliminarExpediente, name = 'eliminar_expediente'),

    # TipoExamen
    url(r'^examenes/tipos/listado$', listadoTipoExamen.as_view(), name = 'listado_tipo_examen'),
    url(r'^examenes/tipos/registrar$', nuevoTipoExamen.as_view(), name = 'nuevo_tipo_examen'),
    url(r'^examenes/ordenes/listado$', listadoSolicitudExamen.as_view(), name = 'listado_orden_examen'),

    # Alergia
    url(r'^alergias/registrar', AlergiaCreate.as_view(), name = 'alergia_crear'),
    url(r'^alergias/listado', AlergiaList.as_view(), name = 'alergia_listar'),
    url(r'^alergias/modificar/(?P<pk>\d+)/$', AlergiaUpdate.as_view() , name = 'alergia_modificar'),

    # Enfermedad
    url(r'^enfermedades/agregar$', AgregarEnfermedad.as_view(), name = 'agregar_enfermedad'),
    url(r'^enfermedades/listado$', ListadoEnfermedades.as_view(), name = 'listado_enfermedades'),
    url(r'^enfermedades/modificar/(?P<pk>\d+)/$', ModificarEnfermedad.as_view(), name = 'modificar_enfermedad'),
    url(r'^enfermedades/eliminar/(?P<id>\d+)/$', eliminarEnfermedad, name = 'eliminar_enfermedad'),

    # EspecialidadEmpleado
    url(r'^empleados/especialidades/agregar$', AgregarEspecialidadEmpleado.as_view(), name = 'agregar_especialidad_empleado'),
    url(r'^empleados/especialidades/listado$', ListadoEspecialidadesEmpleados.as_view(), name = 'listado_especialidades_empleados'),
    url(r'^empleados/especialidades/modificar/(?P<pk>\d+)/$', ModificarEspecialidadEmpleado.as_view(), name = 'modificar_especialidad_empleado'),
    url(r'^empleados/especialidades/eliminar/(?P<id>\d+)/$', eliminarEspecialidadEmpleado, name = 'eliminar_especialidad_empleado'),

    # Medicamento
    url(r'^medicamentos/agregar$', AgregarMedicamento.as_view(), name='agregar_medicamento'),
    url(r'^medicamentos/listado$', ListadoMedicamentos.as_view(), name='listado_medicamentos'),
    url(r'^medicamentos/modificar/(?P<pk>\d+)/$', ModificarMedicamento.as_view(), name='modificar_medicamento'),
    url(r'^medicamentos/eliminar/(?P<id>\d+)/$', eliminarMedicamento, name='eliminar_medicamento'),

    # Empleado
    url(r'^empleados/agregar$', AgregarEmpleado.as_view(), name = 'agregar_empleado'),
    url(r'^empleados/listado$', ListadoEmpleados.as_view(), name = 'listado_empleados'),
    url(r'^empleados/modificar/(?P<pk>\d+)/$', ModificarEmpleado.as_view(), name = 'modificar_empleado'),
    url(r'^empleados/eliminar/(?P<id>\d+)/$', eliminarEmpleado, name = 'eliminar_empleado'),

    # TipoClinica
    url(r'^clinicas/tipos/agregar$', AgregarTipoClinica.as_view(), name = 'agregar_tipo_clinica'),
    url(r'^clinicas/tipos/listado$', ListadoTipoClinicas.as_view(), name = 'listado_tipo_clinicas'),
    url(r'^clinicas/tipos/modificar(?P<pk>\d+)/$', ModificarTipoClinica.as_view(), name = 'modificar_tipo_clinica'),
    url(r'^clinicas/tipos/eliminar(?P<id>\d+)/$', eliminarTipoClinica, name = 'eliminar_tipo_clinica'),

    # Clinica
    url(r'^clinicas/agregar$', AgregarClinica.as_view(), name = 'agregar_clinica'),
    url(r'^clinicas/listado$', ListadoClinica.as_view(), name = 'listado_clinicas'),
    url(r'^clinicas/modificar/(?P<pk>\d+)/$', ModificarClinica.as_view(), name = 'modificar_clinica'),
    url(r'^clinicas/eliminar/(?P<id>\d+)/$', eliminarClinica, name = 'eliminar_clinica'),

    # Consulta
    url(r'^consulta/agregar$', RegistrarConsulta.as_view(), name = 'agregar_consulta'),
    url(r'^consulta/listado$', ListadoConsultas.as_view(), name = 'listado_consultas'),
    url(r'^consulta/modificar/(?P<pk>\d+)/$', ModificarConsulta.as_view(), name = 'modificar_consulta'),
    url(r'^consulta/eliminar/(?P<id>\d+)/$', eliminarConsulta, name = 'eliminar_consulta'),

    # Turno
    url(r'^turnos/agregar$', AgregarTurno.as_view(), name = 'agregar_turno'),
    url(r'^turnos/listado$', ListadoTurnos.as_view(), name = 'listado_turnos'),
    url(r'^turnos/modificar/(?P<pk>\d+)/$', ModificarTurno.as_view(), name = 'modificar_turno'),
    url(r'^turnos/eliminar/(?P<id>\d+)/$', eliminarTurno, name = 'eliminar_turno'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/resultados/listado
