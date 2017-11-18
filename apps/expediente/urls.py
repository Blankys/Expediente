from django.conf.urls import url, include
from apps.expediente.views.GeneralView import index
from apps.expediente.views.ResultadoExamenView import respuestaRegistrarResultadoExamen, listadoExamenes, buscarResultadoExamen# importando vistas
from apps.expediente.views.SignoVitalView import registrarSignoVital, listadoSignosVitales
from apps.expediente.views.ReferenciaMedicaView import registrarReferenciaMedica, listadoReferenciaMedica
from apps.expediente.views.ExpedienteView import registrarExpediente, listadoExpediente
from apps.expediente.views.ExamenMedicoView import listadoTipoExamen, listadoSolicitudExamen, nuevoTipoExamen
from apps.expediente.views.AlergiaView import AlergiaCreate, AlergiaList, AlergiaUpdate, alergia_delete
from apps.expediente.views.CatalogoEnfermedadView import registrarCatalogoEnfermedad, listadoCatalogoEnfermedads
from apps.expediente.views.CatalogoEspecialidadEmpleadoView import registrarCatalogoEspecialidadEmpleado, listadoCatalogoEspecialidadEmpleados
from apps.expediente.views.CatalogoMedicamentoView import registrarCatalogoMedicamento, listadoCatalogoMedicamentos
from apps.expediente.views.EmpleadoView import registrarEmpleado, listadoEmpleados

urlpatterns = [
    url(r'^$', index, name = 'inicio'),  # referenciando a la funcion de vista index del archivo views/GeneralView.py de la apps expediente
    url(r'^examenes/resultados/registrar$', respuestaRegistrarResultadoExamen.as_view(), name = 'registrar_resultado_examen'),    # referenciando a la clase de vista respuestaRegistrarResultadoExamen del archivo views/ResultadoExamenView.py de la apps expediente
    url(r'^examenes/resultados/listado$', listadoExamenes.as_view(), name = 'listado_examenes'), # referenciando a la clase de vista listadoExamenes del archivo views/ResultadoExamenView.py de la apps expediente
    url(r'^examenes/resultados/buscar$', buscarResultadoExamen.as_view(template_name = 'expediente/examenes/buscar.html'), name = 'buscar_examen'),   # referenciando a la clase de vista buscarResultadoExamen del archivo views/ResultadoExamenView.py de la apps expediente
    # NOTA: a la vista de tipo TemplateView no se puede referenciar sin darle un nombre de plantilla que sera la que se encuentra en la carpeta correspondiente de plantillas de la aplicacion
    url(r'^signos-vitales/registrar$', registrarSignoVital, name = 'registrar_signo_vital'),
    url(r'^signos-vitales/listado$', listadoSignosVitales, name = 'listado_signos_vitales'),
    url(r'^referencias/listado$',listadoReferenciaMedica, name = 'listado_referencia_medica'),
    url(r'^referencias/registrar$',registrarReferenciaMedica, name = 'registrar_referencia_medica'),
    url(r'^expedientes/registrar$', registrarExpediente, name= 'registrar_expediente'),
    url(r'^expedientes/listado$', listadoExpediente, name= 'listado_expediente'),
    url(r'^examenes/tipos/listado$', listadoTipoExamen.as_view(), name = 'listado_tipo_examen'),
    url(r'^examenes/tipos/registrar$', nuevoTipoExamen.as_view(), name = 'nuevo_tipo_examen'),
    url(r'^examenes/ordenes/listado$', listadoSolicitudExamen.as_view(), name = 'listado_orden_examen'),
    url(r'^alergias/registrar', AlergiaCreate.as_view(), name='alergia_crear'),
    url(r'^alergias/listado', AlergiaList.as_view(), name='alergia_listar'),
    url(r'^alergias/modificar/(?P<pk>\d+)/$', AlergiaUpdate.as_view() , name='alergia_modificar'),
    #url(r'^alergias/eliminar/(?P<id_alergia>\d+)/$', alergia_delete , name='alergia_eliminar'), no implementado debido a conflicto con modelo expediente
    url(r'^enfermedades/registrar$', registrarCatalogoEnfermedad, name = 'registrar_enfermedad'),
    url(r'^enfermedades/listado$', listadoCatalogoEnfermedads, name = 'listado_enfermedades'),
    url(r'^especialidades-empleados/registrar$', registrarCatalogoEspecialidadEmpleado, name = 'registrar_especialidad_empleado'),
    url(r'^especialidades-empleados/listado$', listadoCatalogoEspecialidadEmpleados, name = 'listado_especialidades_empleados'),
    url(r'^medicamentos/registrar$', registrarCatalogoMedicamento, name = 'registrar_medicamento'),
    url(r'^medicamentos/listado$', listadoCatalogoMedicamentos, name = 'listado_medicamentos'),
    url(r'^empleados/registrar$', registrarEmpleado, name = 'registrar_empleado'),
    url(r'^empleados/listado$', listadoEmpleados, name = 'listado_empleados'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/resultados/listado
