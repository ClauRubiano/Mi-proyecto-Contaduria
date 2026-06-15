from django.db import models

class Tercero(models.Model):
    nit_cedula = models.CharField(max_length=20, unique=True)
    nombre_razon_social = models.CharField(max_length=100)
    def __str__(self): return self.nombre_razon_social

class CuentaContable(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    def __str__(self): return f"{self.codigo} - {self.nombre}"

class AsientoContable(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=200)
    tercero = models.ForeignKey(Tercero, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self): return self.descripcion

class DetalleAsiento(models.Model):
    # Asegúrate de que estos nombres existan y sean correctos
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE)
    cuenta_contable = models.ForeignKey(CuentaContable, on_delete=models.CASCADE)
    tercero = models.ForeignKey(Tercero, on_delete=models.CASCADE) 
    debito = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credito = models.DecimalField(max_digits=15, decimal_places=2, default=0)

class Formulario110(models.Model):
    empleado = models.ForeignKey(Tercero, on_delete=models.CASCADE, verbose_name="Empleado")
    fecha = models.DateField(verbose_name="Fecha de nómina")
    salario_base = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Salario Base")
    auxilio_transporte = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Auxilio de Transporte")
    total_devengado = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Devengado")
    observaciones = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        return f"Nómina de {self.empleado} - {self.fecha}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre