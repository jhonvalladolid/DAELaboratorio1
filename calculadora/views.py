from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sumar(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f"La suma de {num1} + {num2} = {result}")

def restar(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f"La resta de {num1} - {num2} = {result}")

def multiplicar(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f"La multiplicación de {num1} * {num2} = {result}")

