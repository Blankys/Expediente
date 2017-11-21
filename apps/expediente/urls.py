from django.conf.urls import url
from django.contrib.auth.views import login_required
from apps.expediente.views.GeneralView import index, municipios, accesoDenegado
from apps.expediente.views.ResultadoExamenView import respuestaRegistrarResultadoExamen, listadoExamenes, buscarResultadoExamen,uploadResultadosEscaneados,actualizarRegResultExam,listadoArchivoResultados
from apps.expediente.views.SignoVitalView import ListadoSignosVitales, AgregarSignoVital, ModificarSignoVital, eliminarSignoVital
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
from apps.expediente.views.OrdenExamenMedicoView import ListadoOrdenesExamen, AgregarOrdenExamen, ModificarOrdenExamen, eliminarOrdenExamen
from apps.expediente.views.ReferenciaMedicaView import listadoReferenciaMedica, registrarReferenciaMedica, ModificarReferenciaMedica, eliminarReferencia
from apps.expediente.views.ConstanciaMedicaView import ListadoConstanciasMedicas, AgregarConstanciaMedica, ModificarConstanciaMedica, eliminarConstancia
from apps.expediente.views.IncapacidadMedicaView import ListadoIncapacidadesMedicas, AgregarIncapacidadMedica, ModificarIncapacidadMedica, eliminarIncapacidad
from apps.expediente.views.RecetaMedicaView import ListadoRecetasMedicas, AgregarRecetaMedica, ModificarRecetaMedica, eliminarReceta

urlpatterns = [
    # General
    url(r'^$', login_required(index), name='inicio'),
    url(r'^ajax/municipios/$', login_required(municipios), name='ajax_municipios'),
    url(r'^acceso-denegado$', accesoDenegado, name='acceso_denegado'),

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
    url(r'^referencias/agregar$', login_required(registrarReferenciaMedica.as_view()), name='registrar_referencia_medica'),
    url(r'^referencias/listado$', login_required(listadoReferenciaMedica.as_view()), name='listado_referencia_medica'),
    url(r'^referencias/modificar/(?P<pk>\d+)/$', login_required(ModificarReferenciaMedica.as_view()), name='modificar_referencia'),
    url(r'^referencias/eliminar/(?P<id>\d+)/$', login_required(eliminarReferencia), name='eliminar_referencia'),

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

    # OrdenExamen
    url(r'^examenes/ordenes/registrar$', login_required(AgregarOrdenExamen.as_view()), name='agregar_orden_examen'),
    url(r'^examenes/ordenes/listado$', login_required(ListadoOrdenesExamen.as_view()), name='listado_ordenes_examen'),
    url(r'^examenes/ordenes/modificar/(?P<pk>\d+)/$', login_required(ModificarOrdenExamen.as_view()), name='modificar_orden_examen'),
    url(r'^examenes/ordenes/eliminar/(?P<id>\d+)/$', login_required(eliminarOrdenExamen), name='eliminar_orden_examen'),

    # ConstanciaMedica
    url(r'^constancias/agregar$', login_required(AgregarConstanciaMedica.as_view()), name='agregar_constancia'),
    url(r'^constancias/listado$', login_required(ListadoConstanciasMedicas.as_view()), name='listado_constancias'),
    url(r'^constancias/modificar/(?P<pk>\d+)/$', login_required(ModificarConstanciaMedica.as_view()), name='modificar_constancia'),
    url(r'^constancias/eliminar/(?P<id>\d+)/$', login_required(eliminarConstancia), name='eliminar_constancia'),

    # IncapacidadMedica
    url(r'^incapacidad/agregar$', login_required(AgregarIncapacidadMedica.as_view()), name='agregar_incapacidad'),
    url(r'^incapacidad/listado$', login_required(ListadoIncapacidadesMedicas.as_view()), name='listado_incapacidades'),
    url(r'^incapacidad/modificar/(?P<pk>\d+)/$', login_required(ModificarIncapacidadMedica.as_view()), name='modificar_incapacidad'),
    url(r'^incapacidad/eliminar/(?P<id>\d+)/$', login_required(eliminarIncapacidad), name='eliminar_incapacidad'),

    # RecetaMedica
    url(r'^recetas/agregar$', login_required(AgregarRecetaMedica.as_view()), name='agregar_receta'),
    url(r'^recetas/listado$', login_required(ListadoRecetasMedicas.as_view()), name='listado_recetas'),
    url(r'^recetas/modificar/(?P<pk>\d+)/$', login_required(ModificarRecetaMedica.as_view()), name='modificar_receta'),
    url(r'^recetas/eliminar/(?P<id>\d+)/$', login_required(eliminarReceta), name='eliminar_recetas'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/resultados/listado
