from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from .models import Noticia, Requisito, Consulta, PreguntaFrecuente

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'escuela/home.html', {'noticias': noticias})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        Consulta.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            asunto=asunto,
            mensaje=mensaje
        )

        messages.success(request, '¡Tu consulta ha sido enviada con éxito! Nos pondremos en contacto a la brevedad.')

    return render(request, 'escuela/contacto.html')

def portal_login(request):
    return render(request, 'escuela/portal.html')

def requisitos(request):
    req_primario = Requisito.objects.filter(Q(nivel='PRIMARIO') | Q(nivel='AMBOS'))
    req_secundario = Requisito.objects.filter(Q(nivel='SECUNDARIO') | Q(nivel='AMBOS'))
    return render(request, 'escuela/requisitos.html', {
        'req_primario': req_primario,
        'req_secundario': req_secundario
    })

def faq(request):
    faqs = PreguntaFrecuente.objects.filter(activa=True)
    return render(request, 'escuela/faq.html', {'faqs': faqs})