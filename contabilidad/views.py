from django.shortcuts import render, redirect
from django.db.models import Sum
from decimal import Decimal
from .models import DetalleAsiento, AsientoContable
#from .forms import InventarioForm

def index(request):
    return render(request, 'contabilidad/index.html')

def registrar_asiento(request):
    pass

def generar_formulario_110(request):
    # CORREGIDO: cuenta -> cuenta_contable
    ingresos = DetalleAsiento.objects.filter(cuenta_contable__codigo__startswith='4').aggregate(Sum('credito'))['credito__sum'] or 0
    gastos = DetalleAsiento.objects.filter(cuenta_contable__codigo__startswith='5').aggregate(Sum('debito'))['debito__sum'] or 0
    contexto = {
        'ingresos': ingresos,
        'gastos': gastos,
        'utilidad': ingresos - gastos
    }
    return render(request, 'contabilidad/formulario_110.html', contexto)


def liquidar_formulario_310(request):
    # 1. Obtenemos la base de ingresos (créditos en cuentas que inician por 4)
    base_datos = DetalleAsiento.objects.filter(cuenta_contable__codigo__startswith='4') \
        .aggregate(total=Sum('credito'))['total']
    
    # Si es None (no hay registros), lo convertimos a 0
    base = base_datos if base_datos is not None else 0
    
    # 2. Calculamos el impuesto asegurando que ambos sean Decimal
    impuesto = Decimal(str(base)) * Decimal('0.08')
    
    # 3. Enviamos al HTML
    contexto = {
        'base_ingresos': base,
        'impuesto_total': impuesto
    }
    return render(request, 'contabilidad/formulario_310.html', contexto)

def reporte_exogena_dian(request):
    # Agrupamos por tercero y sumamos el débito
    reporte = DetalleAsiento.objects.filter(cuenta_contable__codigo__startswith='5') \
        .values('tercero__nit_cedula', 'tercero__nombre_razon_social') \
        .annotate(pago_acumulado=Sum('debito'))
    
    return render(request, 'contabilidad/reporte_exogena.html', {'reporte': reporte})

def liquidar_formulario_350(request):
    # CORREGIDO: cuenta -> cuenta_contable
    retenciones = DetalleAsiento.objects.filter(cuenta_contable__codigo__startswith='236')
    
    total = retenciones.aggregate(Sum('credito'))['credito__sum'] or 0
    
    contexto = {
        'retenciones': retenciones,
        'total_retenciones': total,
    }
    return render(request, 'contabilidad/formulario_350.html', contexto)

#def vista_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm()
    
    return render(request, 'contabilidad/inventario.html', {'form': form})













