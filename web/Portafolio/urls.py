from django.urls import path
from . import views

app_name = 'Portafolio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('que-conozco/', views.que_conozco, name='que_conozco'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contactos/', views.contactos, name='contactos'),
]