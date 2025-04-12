from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def terms(request):
    return render(request, 'core/terminos-condiciones.html')

def privacy(request):
    return render(request, 'core/privacidad.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')
