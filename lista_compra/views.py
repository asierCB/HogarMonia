from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from pyexpat.errors import messages

from core.models import GrupoHogar, UsuarioGrupo
from .models import ProductoLista, ListaCompra
from .forms import ListaCompraForm, ProductoListaForm

def lista_compra(request):
    user = request.user
    user_group = None
    if user.is_authenticated:
        try:
            user_grupo_relation = UsuarioGrupo.objects.get(usuario_id=user)
            user_group = user_grupo_relation.grupo
        except UsuarioGrupo.DoesNotExist:
            user_group = None  # User is authenticated but not in a group
        except Exception as e:
            print(f"Error getting user group in index view: {e}")
            user_group = None


    context = {
        'grupo': user_group,
    }
    return render(request, 'lista_compra/lista-compra.html', context)


@login_required
def lista_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoHogar, id_grupo=grupo_id)

    # Permission check
    is_member = UsuarioGrupo.objects.filter(usuario=request.user, grupo=grupo).exists()
    if not is_member:
        return HttpResponseForbidden("You do not have permission to view this group's details.")

    # Initialize forms
    form_producto = ProductoListaForm(grupo=grupo)
    form_lista = ListaCompraForm()

    # Handle form submission
    if request.method == "POST":
        if 'nuevo_producto' in request.POST:
            form_producto = ProductoListaForm(request.POST, grupo=grupo)
            if form_producto.is_valid():
                producto = form_producto.save(commit=False)
                # Necesitas obtener la lista seleccionada del formulario
                lista_id = request.POST.get('id_lista')
                if lista_id:
                    try:
                        lista = ListaCompra.objects.get(id_lista=lista_id, id_grupo=grupo)
                        producto.id_lista = lista
                        producto.save()
                        return redirect('lista_grupo', grupo_id=grupo_id)
                    except ListaCompra.DoesNotExist:
                        form_producto.add_error('id_lista', 'Lista no válida')
                else:
                    form_producto.add_error('id_lista', 'Debe seleccionar una lista')
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')

        elif 'nueva_lista' in request.POST:
            form_lista = ListaCompraForm(request.POST)
            if form_lista.is_valid():
                lista = form_lista.save(commit=False)
                lista.id_grupo = grupo
                lista.creada_por = request.user
                lista.save()
                return redirect('lista_grupo', grupo_id=grupo_id)

        elif 'cambiar_estado' in request.POST:
            productos_comprados_ids = request.POST.getlist('productos_comprados')
            lista_id = request.POST.get('lista_id')

            if productos_comprados_ids and lista_id:
                try:
                    # Verificar que la lista pertenezca al grupo actual
                    lista = ListaCompra.objects.get(id_lista=lista_id, id_grupo=grupo)

                    # Convertir a enteros
                    productos_comprados_ids = [int(id) for id in productos_comprados_ids]

                    # Actualizar los productos seleccionados
                    productos_actualizados = ProductoLista.objects.filter(
                        id_producto__in=productos_comprados_ids,
                        id_lista=lista
                    ).update(comprado=True)

                except ListaCompra.DoesNotExist:
                    print("Lista no encontrada")
                except Exception as e:
                    print(f"Error: {e}")

            return redirect('lista_grupo', grupo_id=grupo_id)

        elif 'delete_producto' in request.POST:
            productos_comprados_ids = request.POST.getlist('productos_comprados')
            lista_id = request.POST.get('lista_id')

            if productos_comprados_ids and lista_id:
                try:
                    # Verificar que la lista pertenezca al grupo actual
                    lista = ListaCompra.objects.get(id_lista=lista_id, id_grupo=grupo)

                    # Convertir a enteros
                    productos_comprados_ids = [int(id) for id in productos_comprados_ids]

                    # Eliminar los productos seleccionados
                    productos_actualizados = ProductoLista.objects.filter(
                        id_producto__in=productos_comprados_ids,
                        id_lista=lista
                    ).delete()

                except ListaCompra.DoesNotExist:
                    print("Lista no encontrada")
                except Exception as e:
                    print(f"Error: {e}")

            return redirect('lista_grupo', grupo_id=grupo_id)

    # Get members for display
    relaciones_grupo = UsuarioGrupo.objects.filter(grupo=grupo)
    miembros = User.objects.filter(id__in=relaciones_grupo.values_list('usuario', flat=True))

    # Get listas for the select dropdown
    listas_disponibles = ListaCompra.objects.filter(id_grupo=grupo, activa=True)

    context = {
        'grupo': grupo,
        'miembros': miembros,
        'form_producto': form_producto,
        'form_lista': form_lista,
        'user': request.user,
        'productos': ProductoLista.objects.filter(id_lista__id_grupo=grupo).order_by('comprado', 'tipo'),
        'listas': listas_disponibles,
    }

    return render(request, 'lista_compra/lista-compra.html', context)