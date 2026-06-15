from django.urls import path
from django.contrib import admin  
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reporte-exogena/', views.reporte_exogena_dian, name='reporte_exogena_dian'),
    path('formulario-310/', views.liquidar_formulario_310, name='formulario_310'),
    path('admin/', admin.site.urls), 
    path('formulario-110/', views.generar_formulario_110, name='formulario_110'),
    path('formulario-350/', views.liquidar_formulario_350, name='liquidar_formulario_350'),
    #path('inventario/', views.vista_inventario, name='inventario'),
]