from django.contrib import admin
from django.urls import path, include # Asegúrate de importar include

admin.site.site_header = "SCAcademic - Administración"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Bienvenido a la Gestión Contable"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contabilidad.urls')),
]