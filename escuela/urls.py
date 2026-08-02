from django.urls import path
from . import views

app_name = 'escuela'

urlpatterns = [
    # Páginas públicas
    path('', views.home, name='home'),
    path('requisitos/', views.requisitos, name='requisitos'),
    path('contacto/', views.contacto, name='contacto'),
    path('faq/', views.faq, name='faq'),
    path('docentes/', views.docentes_view, name='docentes'),
    
    # Acceso Staff, Panel Interno y Sesión
    path('portal/', views.portal_login, name='portal'),
    path('logout/', views.cerrar_sesion, name='logout'),
]