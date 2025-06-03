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
            gasto.grupo = grupo
            gasto.save()
            form.save_m2m()
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

        if gasto.pagado_por is not None and request.user == gasto.pagado_por.usuario:
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


@login_required
def edit_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
    grupo = gasto.grupo

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=gasto.grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to edit this gasto.")

    # Handle form submission
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            gasto.delete()
            return redirect('gastos', grupo_id=grupo.id_grupo)

        form = GastoForm(request.POST, instance=gasto, grupo=grupo)
        if form.is_valid():
            # Guardar y actualizar la instancia
            gasto = form.save(commit=False)
            gasto.grupo = grupo
            gasto.save()
            form.save_m2m()

            # Refrescar los participantes después del save
            participantes_usuario_ids = list(
                gasto.participantes.values_list('usuario__id', flat=True)
            )

            return redirect('gastos', grupo_id=grupo.id_grupo)
    else:
        form = GastoForm(instance=gasto, grupo=grupo)

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    # Obtener los usuarios (no UsuarioGrupo) participantes del gasto
    participantes_usuario_ids = list(
        gasto.participantes.values_list('usuario__id', flat=True)
    )

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form': form,
        'user': request.user,
        'gasto': gasto,
        'participantes_usuario_ids': participantes_usuario_ids,
    }

    return render(request, 'gastos/edit-gasto.html', context)



@login_required
def info_deuda(request, grupo_id):
    grupo = get_object_or_404(GrupoHogar, id_grupo=grupo_id)

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to view this group's details.")

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    from decimal import Decimal

    # Inicializar todos los miembros con balance 0
    dicc_deuda = {miembro: Decimal('0.00') for miembro in miembros}

    # Procesar gastos
    gastos = Gasto.objects.filter(grupo=grupo).prefetch_related('participantes__usuario')

    for gasto in gastos:
        participantes_usuario_grupo = gasto.participantes.distinct()
        num_participantes = participantes_usuario_grupo.count()

        if num_participantes == 0:
            continue  # Saltar gastos sin participantes

        share_per_participant = gasto.precio / num_participantes

        # Cada participante debe su parte
        for participante_relacion in participantes_usuario_grupo:
            usuario_participante = participante_relacion.usuario  # Aquí accedes al User
            if usuario_participante in dicc_deuda:  # Solo si es miembro del grupo
                dicc_deuda[usuario_participante] -= Decimal(str(round(share_per_participant)))

        # El que pagó recibe el crédito total
        if gasto.pagado_por is not None:
            usuario_pago = gasto.pagado_por.usuario
            if usuario_pago in dicc_deuda:  # Solo si es miembro del grupo
                dicc_deuda[usuario_pago] += Decimal(str(round(gasto.precio)))

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'user': request.user,
        'deuda': dicc_deuda,
    }

    return render(request, 'gastos/info-deuda.html', context)
