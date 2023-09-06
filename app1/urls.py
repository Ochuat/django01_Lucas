from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_app1, name='index_app1'),
    path("pag/", views.tela01_app1, name='pg01_app1'),
    path("indexZ/", views.index_atividade, name='indexZ_app1'),
    path("help/", views.help, name='help_app1'),
    path("turismo/", views.turismo, name='turismo_app1'),
    path("calculadora/", views.calculadora, name='calculadora_app1'),
    path("formulario/", views.formulario_rh_view, name = 'formulario_rh')
]