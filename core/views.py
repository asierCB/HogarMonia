from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import GrupoHogar, UsuarioGrupo
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def index(request):
    user = request.user
    user_group = None
    if user.is_authenticated:
        try:
            user_grupo_relation = UsuarioGrupo.objects.get(usuario_id=user)
            user_group = user_grupo_relation.grupo
        except UsuarioGrupo.DoesNotExist:
            user_group = None
        except Exception as e:
            user_group = None

    context = {
        'grupo': user_group,
    }

    return render(request, 'core/index.html', context)

def terms(request):
    user = request.user
    user_group = None
    if user.is_authenticated:
        try:
            user_grupo_relation = UsuarioGrupo.objects.get(usuario_id=user)
            user_group = user_grupo_relation.grupo
        except UsuarioGrupo.DoesNotExist:
            user_group = None
        except Exception as e:
            user_group = None

    context = {
        'grupo': user_group,
    }
    return render(request, 'core/terminos-condiciones.html', context)

def privacy(request):
    user = request.user
    user_group = None
    if user.is_authenticated:
        try:
            user_grupo_relation = UsuarioGrupo.objects.get(usuario_id=user)
            user_group = user_grupo_relation.grupo
        except UsuarioGrupo.DoesNotExist:
            user_group = None
        except Exception as e:
            user_group = None

    context = {
        'grupo': user_group,
    }
    return render(request, 'core/privacidad.html', context)

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
            return redirect('perfil')
        else:
            messages.error(request, 'Contraseña o Usuario Incorrectos')
    else:
        form = AuthenticationForm(request)
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def perfil(request):
    from django.contrib.auth.models import User
    from .models import UsuarioGrupo

    # Datos para el perfil
    usuario = request.user
    grupo_usuario = UsuarioGrupo.objects.filter(usuario=usuario).first()
    grupo = grupo_usuario.grupo if grupo_usuario else None
    miembros = grupo.usuariogrupo_set.all() if grupo else None
    rol = grupo_usuario.rol if grupo_usuario else None

    #Gestión Grupos a través del perfil
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'crear':
            nombre_grupo = request.POST.get('nombre_grupo')

            if nombre_grupo == None or nombre_grupo == '':
                messages.error(request, 'No se puede crear grupo sin nombre')
                return redirect('perfil')

            else:
                #Se crea el elemento en la tabla GrupoHogar
                grupo = GrupoHogar.objects.create(nombre_grupo=nombre_grupo)

                #Se crea el elemento en la tabla UsuarioGrupo
                UsuarioGrupo.objects.create(
                    usuario=request.user,
                    grupo=grupo,
                    rol='Admin'
                )
                messages.success(request, 'El grupo se ha creado correctamente.')
                return redirect('perfil')
        elif accion == 'unirse':
            codigo_grupo = request.POST.get('codigo_hogar')

            try:
                grupo = GrupoHogar.objects.get(codigo_invitacion=codigo_grupo)

                #Verificamos que no este el usuario ya en el grupo
                ya_en_grupo = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()

                if not ya_en_grupo:
                    UsuarioGrupo.objects.create(usuario=request.user, grupo=grupo)
                    messages.success(request, 'Te has unido al grupo correctamente.')
                    return redirect('perfil')
                    # Redirigir o recargar con mensaje de éxito
                else:
                    messages.info(request, 'Ya formas parte de este grupo.')
                    pass
            except GrupoHogar.DoesNotExist:
                messages.error(request, 'El código del grupo no es válido.')
                pass

        elif accion == 'salir':
            grupo_usuario = UsuarioGrupo.objects.filter(usuario=request.user).first()

            if grupo_usuario:
                grupo = grupo_usuario.grupo
                if grupo_usuario.rol == 'Admin' and grupo.usuariogrupo_set.count() > 1:
                    nuevo_admin=UsuarioGrupo.objects.filter(grupo=grupo,rol='Miembro').exclude(usuario=usuario).order_by('fecha_union').first()
                    if nuevo_admin:
                        nuevo_admin.rol = 'Admin'
                        nuevo_admin.save()

                grupo_usuario.delete()

                if grupo.usuariogrupo_set.count() == 0:
                    grupo.delete()
                messages.success(request, 'Has salido del grupo correctamente.')
                return redirect('perfil')


    return render(request, 'core/perfil.html',{'grupo' : grupo,'miembros' : miembros, 'rol' : rol})


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña ha sido actualizada exitosamente!')
            return redirect('perfil')  # o donde quieras redirigir
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'core/cambiar_password.html', {'form': form})
