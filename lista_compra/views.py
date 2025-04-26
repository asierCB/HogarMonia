from django.shortcuts import render
from core.models import GrupoHogar, UsuarioGrupo

def lista_compra(request):
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
    return render(request, 'lista_compra/lista-compra.html', context)