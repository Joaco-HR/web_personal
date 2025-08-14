from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def inicio(request):
    """
    Vista para la página de inicio del portafolio
    """
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return render(request, 'Portafolio/index.html', context)

def que_conozco(request):
    """
    Vista para la página de habilidades/conocimientos
    """
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return render(request, 'Portafolio/Que_Conozco.html', context)

def proyectos(request):
    """
    Vista para la página de proyectos
    """
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return render(request, 'Portafolio/Proyectos.html', context)

def contactos(request):
    """
    Vista para la página de contactos
    """
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return render(request, 'Portafolio/contactos.html', context)    