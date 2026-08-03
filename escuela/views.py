from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
    if request.user.is_authenticated:
        return redirect('panel_inicio')

    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        clave_input = request.POST.get('password')

        user = authenticate(request, username=usuario_input, password=clave_input)

        if user is not None:
            login(request, user)
            return redirect('panel_inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'escuela/portal.html')


def cerrar_sesion(request):
    """Cierra la sesión del usuario y redirige al inicio."""
    logout(request)
    return redirect('escuela:home')


# ==========================================
# 4. PANEL DE CONTROL INTERNO (MODALES Y AJAX)
# ==========================================

@login_required
def panel_inicio(request):
    """Menú Principal del Panel de Gestión."""
    return render(request, 'panel/inicio.html')


@login_required
def panel_noticias_lista(request):
    """Listado de noticias para administrar."""
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'panel/noticias_lista.html', {'noticias': noticias})


@login_required
def panel_noticias_crear(request):
    """Crea una noticia mapeando exactamente el campo descripcion de models.py."""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        # Acepta tanto 'descripcion' como 'contenido' por si viene del modal
        descripcion = request.POST.get('descripcion') or request.POST.get('contenido')
        imagen = request.FILES.get('imagen')

        if titulo and descripcion:
            Noticia.objects.create(
                titulo=titulo,
                categoria=categoria,
                descripcion=descripcion,
                imagen=imagen
            )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'ok'}, status=200)
            return redirect('panel_noticias_lista')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Por favor completá los campos obligatorios (*).'
                }, status=400)

    return redirect('panel_noticias_lista')


@login_required
def panel_noticias_borrar(request, pk):
    """Elimina la noticia por AJAX directamente desde la tabla."""
    if request.method == 'POST':
        try:
            noticia = Noticia.objects.get(pk=pk)
            noticia.delete()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'ok'}, status=200)
            return redirect('panel_noticias_lista')
        except Noticia.DoesNotExist:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'La noticia ya no existe.'}, status=404)
            return redirect('panel_noticias_lista')
            
    return redirect('panel_noticias_lista')