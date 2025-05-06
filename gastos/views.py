from tokenize import group
#views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from core.models import GrupoHogar, UsuarioGrupo, User
from .models import Gasto
from .forms import GastoForm

@login_required
def gastos(request):
    users = User.objects.all()
    groups = GrupoHogar.objects.all()
    UserGroup = UsuarioGrupo.objects.all()

    context = {
        'User': users,
        'GrupoHogar': groups,
        'UsuarioGrupo': UserGroup
    }

    return render(request, 'gastos/gastos.html', context)


@login_required
def miembros_del_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoHogar, id_grupo=grupo_id)

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to view this group's details.")

    # Handle form submission
    if request.method == 'POST':
        form = GastoForm(request.POST, grupo=grupo)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.grupo = grupo  # If you have a grupo field in your Gasto model
            gasto.save()
            form.save_m2m()  # Important to save ManyToMany relationships
            return redirect('gastos', grupo_id=grupo_id)
    else:
        form = GastoForm(grupo=grupo)

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    deuda = 0
    for gasto in Gasto.objects.filter(grupo=grupo):
        for participante in gasto.participantes.all():
            if participante.usuario == request.user:
                deuda += gasto.precio / gasto.participantes.all().count()
                break

        if request.user == gasto.pagado_por:
            deuda -= gasto.precio

    deuda = round(deuda, 2)




    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form': form,
        'user': request.user,

        'gastos': Gasto.objects.filter(grupo=grupo).order_by('-fecha_gasto'),

        'deuda': deuda,
    }
    return render(request, 'gastos/gastos.html', context)
