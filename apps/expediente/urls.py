from django.conf.urls import url
from django.contrib.auth.views import login_required
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
    url(r'^$', login_required(index), name='inicio'),
    url(r'^ajax/municipios/$', login_required(municipios), name='ajax_municipios'),

    # ResultadoExamen
    url(r'^examenes/resultados/registrar$', login_required(respuestaRegistrarResultadoExamen.as_view()), name='registrar_resultado_examen'),
    url(r'^examenes/resultados/listado$', login_required(listadoExamenes.as_view()), name='listado_examenes'),
    url(r'^examenes/resultados/buscar$', login_required(buscarResultadoExamen.as_view(template_name='expediente/examenes/buscar.html')), name='buscar_examen'),
    url(r'^examenes/resultados/subir$', login_required(uploadResultadosEscaneados.as_view()), name='resultados_escaneados'),
    url(r'^examenes/resultados/modificar/(?P<pk>\d+)$', login_required(actualizarRegResultExam.as_view()), name='modificar_examen'),
    url(r'^examenes/resultados/listado_archivos$', login_required(listadoArchivoResultados.as_view()), name='listado_archivos'),

    # SignoVital
    url(r'^signos-vitales/agregar$', login_required(AgregarSignoVital.as_view()), name='agregar_signo_vital'),
    url(r'^signos-vitales/listado$', login_required(ListadoSignosVitales.as_view()), name='listado_signos_vitales'),
    url(r'^signos-vitales/modificar/(?P<pk>\d+)/$', login_required(ModificarSignoVital.as_view()), name='modificar_signo_vital'),
    url(r'^signos-vitales/eliminar/(?P<id>\d+)/$', login_required(eliminarSignoVital), name='eliminar_signo_vital'),

    # ReferenciaMedica
    url(r'^referencias/listado$', login_required(listadoReferenciaMedica), name='listado_referencia_medica'),
    url(r'^referencias/registrar$', login_required(registrarReferenciaMedica), name='registrar_referencia_medica'),

    # Expediente
    url(r'^expedientes/agregar$', login_required(agregarExpediente), name='agregar_expediente'),
    url(r'^expedientes/listado$', login_required(listadoExpedientes.as_view()), name='listado_expedientes'),
    url(r'^expedientes/modificar/(?P<id>\d+)/$', login_required(modificarExpediente), name='modificar_expediente'),
    url(r'^expedientes/eliminar/(?P<id>\d+)/$', login_required(eliminarExpediente), name='eliminar_expediente'),

    # TipoExamen
    url(r'^examenes/tipos/listado$', login_required(listadoTipoExamen.as_view()), name='listado_tipo_examen'),
    url(r'^examenes/tipos/registrar$', login_required(nuevoTipoExamen.as_view()), name='nuevo_tipo_examen'),
    url(r'^examenes/ordenes/listado$', login_required(listadoSolicitudExamen.as_view()), name='listado_orden_examen'),

    # Alergia
    url(r'^alergias/registrar', login_required(AlergiaCreate.as_view()), name='alergia_crear'),
    url(r'^alergias/listado', login_required(AlergiaList.as_view()), name='alergia_listar'),
    url(r'^alergias/modificar/(?P<pk>\d+)/$', login_required(AlergiaUpdate.as_view() ), name='alergia_modificar'),

    # Enfermedad
    url(r'^enfermedades/agregar$', login_required(AgregarEnfermedad.as_view()), name='agregar_enfermedad'),
    url(r'^enfermedades/listado$', login_required(ListadoEnfermedades.as_view()), name='listado_enfermedades'),
    url(r'^enfermedades/modificar/(?P<pk>\d+)/$', login_required(ModificarEnfermedad.as_view()), name='modificar_enfermedad'),
    url(r'^enfermedades/eliminar/(?P<id>\d+)/$', login_required(eliminarEnfermedad), name='eliminar_enfermedad'),

    # EspecialidadEmpleado
    url(r'^empleados/especialidades/agregar$', login_required(AgregarEspecialidadEmpleado.as_view()), name='agregar_especialidad_empleado'),
    url(r'^empleados/especialidades/listado$', login_required(ListadoEspecialidadesEmpleados.as_view()), name='listado_especialidades_empleados'),
    url(r'^empleados/especialidades/modificar/(?P<pk>\d+)/$', login_required(ModificarEspecialidadEmpleado.as_view()), name='modificar_especialidad_empleado'),
    url(r'^empleados/especialidades/eliminar/(?P<id>\d+)/$', login_required(eliminarEspecialidadEmpleado), name='eliminar_especialidad_empleado'),

    # Medicamento
    url(r'^medicamentos/agregar$', login_required(AgregarMedicamento.as_view()), name='agregar_medicamento'),
    url(r'^medicamentos/listado$', login_required(ListadoMedicamentos.as_view()), name='listado_medicamentos'),
    url(r'^medicamentos/modificar/(?P<pk>\d+)/$', login_required(ModificarMedicamento.as_view()), name='modificar_medicamento'),
    url(r'^medicamentos/eliminar/(?P<id>\d+)/$', login_required(eliminarMedicamento), name='eliminar_medicamento'),

    # Empleado
    url(r'^empleados/agregar$', login_required(AgregarEmpleado.as_view()), name='agregar_empleado'),
    url(r'^empleados/listado$', login_required(ListadoEmpleados.as_view()), name='listado_empleados'),
    url(r'^empleados/modificar/(?P<pk>\d+)/$', login_required(ModificarEmpleado.as_view()), name='modificar_empleado'),
    url(r'^empleados/eliminar/(?P<id>\d+)/$', login_required(eliminarEmpleado), name='eliminar_empleado'),

    # TipoClinica
    url(r'^clinicas/tipos/agregar$', login_required(AgregarTipoClinica.as_view()), name='agregar_tipo_clinica'),
    url(r'^clinicas/tipos/listado$', login_required(ListadoTipoClinicas.as_view()), name='listado_tipo_clinicas'),
    url(r'^clinicas/tipos/modificar(?P<pk>\d+)/$', login_required(ModificarTipoClinica.as_view()), name='modificar_tipo_clinica'),
    url(r'^clinicas/tipos/eliminar(?P<id>\d+)/$', login_required(eliminarTipoClinica), name='eliminar_tipo_clinica'),

    # Clinica
    url(r'^clinicas/agregar$', login_required(AgregarClinica.as_view()), name='agregar_clinica'),
    url(r'^clinicas/listado$', login_required(ListadoClinica.as_view()), name='listado_clinicas'),
    url(r'^clinicas/modificar/(?P<pk>\d+)/$', login_required(ModificarClinica.as_view()), name='modificar_clinica'),
    url(r'^clinicas/eliminar/(?P<id>\d+)/$', login_required(eliminarClinica), name='eliminar_clinica'),

    # Consulta
    url(r'^consulta/agregar$', login_required(RegistrarConsulta.as_view()), name='agregar_consulta'),
    url(r'^consulta/listado$', login_required(ListadoConsultas.as_view()), name='listado_consultas'),
    url(r'^consulta/modificar/(?P<pk>\d+)/$', login_required(ModificarConsulta.as_view()), name='modificar_consulta'),
    url(r'^consulta/eliminar/(?P<id>\d+)/$', login_required(eliminarConsulta), name='eliminar_consulta'),

    # Turno
    url(r'^turnos/agregar$', login_required(AgregarTurno.as_view()), name='agregar_turno'),
    url(r'^turnos/listado$', login_required(ListadoTurnos.as_view()), name='listado_turnos'),
    url(r'^turnos/modificar/(?P<pk>\d+)/$', login_required(ModificarTurno.as_view()), name='modificar_turno'),
    url(r'^turnos/eliminar/(?P<id>\d+)/$', login_required(eliminarTurno), name='eliminar_turno'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/resultados/listado
