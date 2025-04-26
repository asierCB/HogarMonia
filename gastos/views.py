from tokenize import group

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from core.models import GrupoHogar, UsuarioGrupo, User

@login_required
def gastos(request):
    users = User.objects.all()
    groups = GrupoHogar.objects.all()
    UserGroup = UsuarioGrupo.objects.all()

    context = {'User': users, 'GrupoHogar': groups, 'UsuarioGrupo': UserGroup}
    return render(request, 'gastos/gastos.html', context)

@login_required
def miembros_del_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoHogar, id_grupo=grupo_id)

    # Check if a UsuarioGrupo relation exists for the current user and this group
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()

    # If the user is NOT a member of this group, deny access
    if not is_member:
        print(
            f"--- Permission Denied: User {request.user.username} (ID: {request.user.id}) is not a member of group {grupo.nombre_grupo} (ID: {grupo_id}) ---")
        # Return a 403 Forbidden response
        return HttpResponseForbidden("You do not have permission to view this group's details.")
    # --- End Permission Check ---

    print("--- Entering miembros_del_grupo view ---")
    try:
        grupo = GrupoHogar.objects.get(id_grupo=grupo_id)
        print(f"--- Debugging for group ID: {grupo_id} ---")
        print(f"Retrieved group: {grupo}")

        relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
        print(f"Relaciones_grupo QuerySet: {relaciones_grupo}")
        print(f"Relaciones_grupo count: {relaciones_grupo.count()}")


        user_ids = relaciones_grupo.values_list('usuario', flat=True)
        print(f"User IDs list: {user_ids}")

        miembros = User.objects.filter(id__in=user_ids)
        print(f"Miembros QuerySet: {miembros}")
        print(f"Miembros count: {miembros.count()}")

        context = {
            'grupo': grupo,
            'miembros': miembros,
        }
        return render(request, 'gastos/gastos.html', context)
    except GrupoHogar.DoesNotExist:
        print(f"--- Error: GrupoHogar with ID {grupo_id} does not exist ---")
        # Handle the case where the group doesn't exist
        # You might want to return a 404 or render an error page
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound("Group not found")
    except Exception as e:
        print(f"--- An unexpected error occurred: {e} ---")
        raise
'''def miembros_del_grupo(request, grupo_id):
    try:
        grupo = GrupoHogar.objects.get(id_grupo=grupo_id)
        # Obtén todas las relaciones UsuarioGrupo para este grupo
        relaciones_grupo = UsuarioGrupo.objects.filter(id_grupo=grupo)
        print(relaciones_grupo.count)
        # Obtén los IDs de usuario de las relaciones
        user_ids = relaciones_grupo.values_list('id_usuario', flat=True)
        print(user_ids)
        # Obtén los usuarios asociados usando the collected IDs
        miembros = User.objects.filter(id__in=user_ids)
        print(miembros.count)


        # Obtén los usuarios asociados a través de estas relaciones
        #miembros = [relacion.id_usuario for relacion in relaciones_grupo]

        context = {
            'grupo': grupo,
            'miembros': miembros,
        }
        return render(request, 'core/gastos.html', context)

    except GrupoHogar.DoesNotExist:
        # Manejar el caso en que el grupo no existe
        return render(request, 'core/grupo_no_encontrado.html')'''

