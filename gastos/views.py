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

    context = {'User': users, 'GrupoHogar': groups, 'UsuarioGrupo': UserGroup}
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

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form': form,
        'user': request.user,

        'gastos': Gasto.objects.filter(grupo=grupo).order_by('-fecha_gasto'),
    }
    return render(request, 'gastos/gastos.html', context)

'''def gastos_view(request, id_grupo=None):
    if request.method == "POST":
        concepto = request.POST.get('concepto')
        precio = request.POST.get('precio')
        pagado_por_id = request.POST.get('pagado_por')
        recurrente = request.POST.get('recurrente') == 'on'
        participantes_ids = request.POST.getlist('participantes')

        print("----- DATOS RECIBIDOS EN EL POST -----")
        print("Concepto:", concepto)
        print("Precio:", precio)
        print("Pagado por (ID):", pagado_por_id)
        print("Recurrente:", recurrente)
        print("Participantes IDs:", participantes_ids)

        if concepto and precio and pagado_por_id:
            # Creamos el gasto
            gasto = Gasto.objects.create(
                concepto=concepto,
                precio=precio,
                pagado_por=User.objects.get(id=pagado_por_id),
                recurrente=recurrente
            )

            # Añadimos los participantes
            participantes_objs = UsuarioGrupo.objects.filter(id__in=participantes_ids)
            gasto.participantes.set(participantes_objs)

            gasto.save()

            return redirect('gastos', id_grupo=id_grupo)  # Redirige a donde quieras tras guardar

    # Si es GET o algo va mal
    # Aquí tu código para mostrar el formulario con los miembros, como ya tienes
    miembros = User.objects.filter(usuariogrupo__id_grupo=id_grupo)
    return render(request, 'gastos/gastos.html', {'miembros': miembros})'''
