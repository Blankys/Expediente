from django.conf.urls import url, include
from apps.expediente.views import index, registrarResultadoExamen, listadoExamenes

urlpatterns = [
    url(r'^$', index),
    url(r'^examenes/registrar$', registrarResultadoExamen, name = 'registrar_resultado_examen'),
    url(r'^examenes/listado$', listadoExamenes, name = 'listado_examenes'),
]

# Para acceder a una vista, desde la barra de direcciones del navegador digitar:
# http://localhost:8000/{url_absoluta}
# Donde {url_absoluta} es: {url_global}/{url_app}
# Por ejemplo: http://localhost:8000/examenes/listado
