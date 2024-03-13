from django.urls import path
from . import views

urlpatterns = [
    path('<int:tarifa>/<int:horas>/', views.calc_salario, name='calc_salario'),
]
