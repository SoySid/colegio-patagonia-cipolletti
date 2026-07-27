from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Página Institucional de la Escuela</h1><p>Bienvenidos al sitio web oficial.</p>")

def contacto(request):
    return HttpResponse("<h1>Contacto</h1><p>Consultas: contacto@escuela.edu.ar</p>")

def portal_login(request):
    return HttpResponse("<h1>Portal Alumnos</h1><p>Ingreso con usuario y contraseña.</p>")