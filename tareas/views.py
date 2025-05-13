from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from core.models import GrupoHogar, UsuarioGrupo, User
from .models import Tareas
from .forms import TareaForm

# Create your views here.
@login_required
def tareas(request):
    user = request.user
    user_group = None
    if user.is_authenticated:
        try:
            # Assuming a relation from User to UsuarioGrupo, and then to GrupoHogar
            # You might need to adjust this based on your model relationships
            user_grupo_relation = UsuarioGrupo.objects.get(usuario_id=user)
            user_group = user_grupo_relation.grupo  # This should be the GrupoHogar object
        except UsuarioGrupo.DoesNotExist:
            user_group = None  # User is authenticated but not in a group
        except Exception as e:
            print(f"Error getting user group in index view: {e}")
            user_group = None

    # Check the value you're passing to the template for the group ID
    # Assuming your template uses something like {% url 'gastos' context_group.id_grupo %}

    print(f"--- Debugging index view context ---")
    print(f"Variable 'context_group': {user_group}")
    if user_group:
        print(f"Variable 'context_group.id_grupo': {user_group.id_grupo}")  # Or context_group.id
    else:
        print("Variable 'context_group' is None or empty")
    print("--- End index view debugging ---")

    context = {
        # ... other context variables ...
        'grupo': user_group,  # Make sure you pass the group or group ID correctly
        # 'user_group_id': context_group.id_grupo if context_group else None # Or pass the ID directly
    }
    return render(request, 'tareas/tareas.html', context)

@login_required
def tareas_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoHogar, id_grupo=grupo_id)

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to view this group's details.")

    # Handle form submission
    if request.method == 'POST':
        form = TareaForm(request.POST, grupo=grupo)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.grupo = grupo  # If you have a grupo field in your Gasto model
            tarea.save()
            form.save_m2m()  # Important to save ManyToMany relationships
            return redirect('tareas', grupo_id=grupo_id)
    else:
        form = TareaForm(grupo=grupo)

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form': form,
        'user': request.user,

        'tareas': Tareas.objects.filter(grupo=grupo), #.order_by('-fecha_gasto'),

    }
    return render(request, 'tareas/tareas.html', context)

@login_required
def edit_tarea(request, tarea_id,):
    tarea = get_object_or_404(Tareas, id_tareas=tarea_id)
    grupo = tarea.grupo

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=tarea.grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to edit this tarea.")

    # Handle form submission
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea, grupo=grupo)
        if form.is_valid():
            tarea2 = form.save(commit=False)
            tarea2.grupo = grupo  # If you have a grupo field in your Gasto model
            tarea2.save()
            form.save_m2m()  # Important to save ManyToMany relationships
            return redirect('tareas', grupo_id=grupo.id_grupo)
    else:
        form = TareaForm(instance=tarea, grupo=grupo)

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form': form,
        'user': request.user,

        'tarea': tarea,  # .order_by('-fecha_gasto'),

    }

    return render(request, 'tareas/edit-tarea.html', context)

