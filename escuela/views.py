from django.shortcuts import render
from django.db.models import Q
from .models import Noticia, Requisito

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'escuela/home.html', {'noticias': noticias})

def contacto(request):
    return render(request, 'escuela/contacto.html')

def portal_login(request):
    return render(request, 'escuela/portal.html')

def requisitos(request):
    # Trae los específicos de Primario MÁS los que son para Ambos
    req_primario = Requisito.objects.filter(Q(nivel='PRIMARIO') | Q(nivel='AMBOS'))
    
    # Trae los específicos de Secundario MÁS los que son para Ambos
    req_secundario = Requisito.objects.filter(Q(nivel='SECUNDARIO') | Q(nivel='AMBOS'))

    return render(request, 'escuela/requisitos.html', {
        'req_primario': req_primario,
        'req_secundario': req_secundario
    })