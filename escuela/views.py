from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Noticia, Requisito, Consulta, PreguntaFrecuente, CarruselInicio, PostulacionDocente, Docente

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    carrusel = CarruselInicio.objects.filter(activa=True).order_by('orden')
    return render(request, 'escuela/home.html', {
        'noticias': noticias,
        'carrusel': carrusel,
    })

def contacto(request):
    if request.method == 'POST':
        tipo_form = request.POST.get('tipo_form')

        if tipo_form == 'docente':
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            nivel_interes = request.POST.get('asunto')
            mensaje = request.POST.get('mensaje')
            cv = request.FILES.get('cv')

            if cv:
                PostulacionDocente.objects.create(
                    nombre=nombre,
                    email=email,
                    telefono=telefono,
                    nivel_interes=nivel_interes,
                    area_materia='Docente',
                    cv=cv,
                    mensaje=mensaje
                )
                messages.success(request, '¡Tu postulación fue enviada con éxito! Nos pondremos en contacto a la brevedad.')
            else:
                messages.error(request, 'Debes adjuntar un CV para enviar la postulación.')
        else:
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
    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        clave_input = request.POST.get('password')

        user = authenticate(request, username=usuario_input, password=clave_input)

        if user is not None:
            login(request, user)
            
            # Si es Admin o Staff (docente habilitado/preceptor), entra directo al Panel de Control
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')
            
            # Si es Alumno/Tutor común
            messages.success(request, f'Bienvenido/a {user.username}.')
            return redirect('portal')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

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

def docentes_view(request):
    docentes = Docente.objects.filter(activo=True)
    return render(request, 'escuela/docentes.html', {'docentes': docentes})