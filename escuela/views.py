from django.shortcuts import render
from .models import Noticia

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'escuela/home.html', {'noticias': noticias})

def contacto(request):
    return render(request, 'escuela/contacto.html')

def portal_login(request):
    return render(request, 'escuela/portal.html')

def requisitos(request):
    return render(request, 'escuela/requisitos.html')