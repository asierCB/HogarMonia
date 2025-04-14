from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def terms(request):
    return render(request, 'core/terminos-condiciones.html')

def privacy(request):
    return render(request, 'core/privacidad.html')

'''def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')'''

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Registro exitoso, redirigiendo...")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tareas')
    else:
        form = AuthenticationForm(request)
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def perfil(request):
    return render(request, 'core/perfil.html')
