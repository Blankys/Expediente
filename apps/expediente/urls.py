from django.conf.urls import url, include
from apps.expediente.views.GeneralView import index
from apps.expediente.views.ResultadoExamenView import respuestaRegistrarResultadoExamen, listadoExamenes, buscarResultadoExamen  # importando vistas
from apps.expediente.views.SignoVitalView import registrarSignoVital, listadoSignosVitales

urlpatterns = [
    url(r'^$', index),  # referenciando a la funcion de vista index del archivo views/GeneralView.py de la apps expediente
    url(r'^examenes/registrar$', respuestaRegistrarResultadoExamen.as_view(), name = 'registrar_resultado_examen'),    # referenciando a la clase de vista respuestaRegistrarResultadoExamen del archivo views/ResultadoExamenView.py de la apps expediente
    url(r'^examenes/listado$', listadoExamenes.as_view(), name = 'listado_examenes'), # referenciando a la clase de vista listadoExamenes del archivo views/ResultadoExamenView.py de la apps expediente
    url(r'^examenes/buscar$', buscarResultadoExamen.as_view(template_name = 'expediente/examenes/buscar.html'), name = 'buscar_examen'),   # referenciando a la clase de vista buscarResultadoExamen del archivo views/ResultadoExamenView.py de la apps expediente
    # NOTA: a la vista de tipo TemplateView no se puede referenciar sin darle un nombre de plantilla que sera la que se encuentra en la carpeta correspondiente de plantillas de la aplicacion
    url(r'^signos-vitales/registrar$', registrarSignoVital, name = 'registrar_signo_vital'),
    url(r'^signos-vitales/listado$', listadoSignosVitales, name = 'listado_signos_vitales'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/listado
