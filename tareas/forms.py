from django import forms

from core.models import UsuarioGrupo
from .models import Tareas
from django.contrib.auth.models import User

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['nombre_tareas', 'fecha_limite', 'es_periodica','completada', 'tiempo_estimado', 'npersonas', 'frecuencia', 'participantes']  # Campos del formulario

    def __init__(self, *args, **kwargs):
        grupo = kwargs.pop('grupo', None)  # sacamos el grupo del constructor
        super().__init__(*args, **kwargs)
        if grupo:
            # Solo mostramos los usuarios que pertenecen al grupo
            self.fields['participantes'].queryset = UsuarioGrupo.objects.filter(grupo=grupo)#usuariogrupo__id_grupo=grupo)
