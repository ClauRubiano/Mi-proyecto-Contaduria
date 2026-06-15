from django.contrib import admin
from .models import Tercero, CuentaContable, AsientoContable, DetalleAsiento, Producto

class DetalleAsientoInline(admin.TabularInline):
    model = DetalleAsiento
    extra = 1

@admin.register(AsientoContable)
class AsientoContableAdmin(admin.ModelAdmin):
    inlines = [DetalleAsientoInline]

admin.site.register(Tercero)
admin.site.register(CuentaContable)

