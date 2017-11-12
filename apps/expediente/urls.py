from django.conf.urls import url,include
from apps.expediente.views import index,ver_form_registro_result_labo,ver_listado_reg_result_lab #importando vistas


urlpatterns = [
    url(r'^$',index),#referenciando a la funcion de vista index del archivo views.py de la apps expediente
    url(r'^registro$',ver_form_registro_result_labo, name='reg_result_lab'),#referenciando a la funcion de vista ver_form_registro_result_labo del archivo views.py de la apps expediente
    url(r'^listar$',ver_listado_reg_result_lab, name='list_reg_lab'),#referenciando a la funcion de vista ver_listado_reg_result_lab del archivo views.py de la apps expediente
]

#para acceder a la vista desde el navegador:
#localhost:8000/url del archivo de urls de la app contenida entre los caracteres ^$