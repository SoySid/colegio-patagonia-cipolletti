from django.urls import path
from . import views

app_name = 'escuela'

urlpatterns = [
    path('', views.home, name='home'),
    path('requisitos/', views.requisitos, name='requisitos'),
    path('contacto/', views.contacto, name='contacto'),
    path('portal/', views.portal_login, name='portal'),
    path('faq/', views.faq, name='faq'),
    path('docentes/', views.docentes_view, name='docentes'),
]