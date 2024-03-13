from django.urls import path
from . import views

urlpatterns = [
    path('sumar/<int:num1>/<int:num2>/', views.sumar, name='sumar'),
    path('restar/<int:num1>/<int:num2>/', views.restar, name='restar'),
    path('multiplicar/<int:num1>/<int:num2>/', views.multiplicar, name='multiplicar'),
]
