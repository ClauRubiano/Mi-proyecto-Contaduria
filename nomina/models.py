from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Importamos los modelos de tu app contabilidad
from contabilidad.models import AsientoContable, DetalleAsiento, CuentaContable, Tercero

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

class Liquidacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_liquidacion = models.DateField(auto_now_add=True)
    neto_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Liq. {self.empleado.nombre} - {self.fecha_liquidacion}"

# Esta señal hace que al guardar una liquidación, se cree el asiento automáticamente
@receiver(post_save, sender=Liquidacion)
def crear_asiento_automatico(sender, instance, created, **kwargs):
    if created:
        # 1. Creamos el asiento contable
        asiento = AsientoContable.objects.create(
            descripcion=f"Liquidación de nómina para {instance.empleado.nombre}",
            tercero=Tercero.objects.get_or_create(nit_cedula=instance.empleado.cedula, defaults={'nombre_razon_social': instance.empleado.nombre})[0]
        )
        # 2. Aquí iría la lógica para crear los DetalleAsiento con las cuentas 5105 y 2505