from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import (
    Noticia, 
    Requisito, 
    Consulta, 
    PreguntaFrecuente, 
    CarruselInicio, 
    PostulacionDocente, 
    Docente
)

# ==========================================
# 1. PÁGINAS PÚBLICAS Y CONTENIDO INSTITUCIONAL
# ==========================================

def home(request):
    """Página principal con noticias y carrusel activo."""
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    carrusel = CarruselInicio.objects.filter(activa=True).order_by('orden')
    return render(request, 'escuela/home.html', {
        'noticias': noticias,
        'carrusel': carrusel,
    })


def requisitos(request):
    """Muestra los requisitos de inscripción organizados por los 3 niveles."""
    req_inicial = Requisito.objects.filter(Q(nivel='INICIAL') | Q(nivel='AMBOS'))
    req_primario = Requisito.objects.filter(Q(nivel='PRIMARIO') | Q(nivel='AMBOS'))
    req_medio = Requisito.objects.filter(Q(nivel='MEDIO') | Q(nivel='SECUNDARIO') | Q(nivel='AMBOS'))
    
    return render(request, 'escuela/requisitos.html', {
        'req_inicial': req_inicial,
        'req_primario': req_primario,
        'req_medio': req_medio,
    })


def faq(request):
    """Listado de Preguntas Frecuentes activas."""
    faqs = PreguntaFrecuente.objects.filter(activa=True)
    return render(request, 'escuela/faq.html', {'faqs': faqs})


def docentes_view(request):
    """Listado de autoridades y cuerpo docente activo."""
    docentes = Docente.objects.filter(activo=True)
    return render(request, 'escuela/docentes.html', {'docentes': docentes})


# ==========================================
# 2. CONTACTO Y FORMULARIOS DE RECEPCIÓN
# ==========================================

def contacto(request):
    """Manejo de consultas generales y postulaciones docentes."""
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


# ==========================================
# 3. ACCESO STAFF Y GESTIÓN DE SESIÓN
# ==========================================

def portal_login(request):
    """Acceso exclusivo para el personal del colegio (Staff)."""
    # Si el usuario ya está autenticado, lo manda directo al panel nuevo
    if request.user.is_authenticated:
        return redirect('panel_inicio')

    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        clave_input = request.POST.get('password')

        user = authenticate(request, username=usuario_input, password=clave_input)

        if user is not None:
            login(request, user)  # Guarda la sesión firmada en las cookies
            return redirect('panel_inicio')  # Redirección al panel nuevo
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'escuela/portal.html')


def cerrar_sesion(request):
    """Cierra la sesión del usuario y redirige al inicio."""
    logout(request)
    return redirect('escuela:home')