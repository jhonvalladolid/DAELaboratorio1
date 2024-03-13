from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def calc_salario(request, tarifa, horas):
    # Convertir las entradas a números enteros
    tarifa = int(tarifa)
    horas = int(horas)
    
    # Calcular el salario normal.
    if horas <= 40:
        salario_tot = tarifa * horas
    else:
        # Calcular el salario con pago de horas extras.
        horas_ext = horas - 40
        salario_tot = (tarifa * 40) + (tarifa * 2 * horas_ext)
    
    return HttpResponse(f"El salario semanal total para {horas} horas a {tarifa} por hora es: {salario_tot}")
