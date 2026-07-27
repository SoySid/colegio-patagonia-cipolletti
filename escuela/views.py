from django.shortcuts import render

def home(request):
    return render(request, 'escuela/home.html')

def contacto(request):
    return render(request, 'escuela/contacto.html')

def portal_login(request):
    return render(request, 'escuela/portal.html')

def requisitos(request):
    return render(request, 'escuela/requisitos.html')