from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import GrupoHogar


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
    from django.contrib.auth.models import User
    from .models import UsuarioGrupo

    # Datos para el perfil
    usuario = request.user
    grupo_usuario = UsuarioGrupo.objects.filter(usuario=usuario).first()
    grupo = grupo_usuario.grupo if grupo_usuario else None
    miembros = grupo.usuariogrupo_set.all() if grupo else None
    rol = grupo_usuario.rol if grupo_usuario else None

    #Gestión Grupos a través del perfiles

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'crear':
            nombre_grupo = request.POST.get('nombre_grupo')

            #Se crea el elemento en la tabla GrupoHogar
            grupo = GrupoHogar.objects.create(nombre_grupo=nombre_grupo)

            #Se crea el elemento en la tabla UsuarioGrupo
            UsuarioGrupo.objects.create(
                usuario=request.user,
                grupo=grupo,
                rol='Admin'
            )
            return redirect('perfil')
        elif accion == 'unirse':
            codigo_grupo = request.POST.get('codigo_hogar')

            try:
                grupo = GrupoHogar.objects.get(codigo_invitacion=codigo_grupo)

                #Verificamos que no este el usuario ya en el grupo
                ya_en_grupo = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()

                if not ya_en_grupo:
                    UsuarioGrupo.objects.create(usuario=request.user, grupo=grupo)
                    print("Unido con exito")
                    return redirect('perfil')
                    # Redirigir o recargar con mensaje de éxito
                else:
                    pass
            except GrupoHogar.DoesNotExist:
                # Mostrar mensaje de error
                print("Grupo no encontrado")
                pass

        elif accion == 'salir':
            grupo_usuario = UsuarioGrupo.objects.filter(usuario=request.user).first()

            if grupo_usuario:
                grupo = grupo_usuario.grupo
                grupo_usuario.delete()

                if grupo.usuariogrupo_set.count() == 0:
                    grupo.delete()

                return redirect('perfil')


    return render(request, 'core/perfil.html',{'grupo' : grupo,'miembros' : miembros, 'rol' : rol})
