from django import forms

from core.models import UsuarioGrupo
from .models import Tareas
from django.contrib.auth.models import User

class TareaForm(forms.ModelForm):
    #participantes = forms.ModelMultipleChoiceField(
        #queryset=UsuarioGrupo.objects.none(),
        #widget=forms.CheckboxSelectMultiple(attrs={
        #    'class': 'custom-checkbox',
       #     'style': 'display: flex; flex-direction: column; gap: 8px;'
            # 'style': 'display: flex; flex-direction: column;'
      #  }),
     #   required=False
    #)
    class Meta:
        model = Tareas
        fields = ['nombre_tareas', 'fecha_limite', 'es_periodica','completada', 'tiempo_estimado', 'frecuencia', 'participantes']  # Campos del formulario

    def __init__(self, *args, **kwargs):
        grupo = kwargs.pop('grupo', None)  # sacamos el grupo del constructor
        super().__init__(*args, **kwargs)
        if grupo:
            # Solo mostramos los usuarios que pertenecen al grupo
            self.fields['participantes'].queryset = UsuarioGrupo.objects.filter(grupo=grupo)#usuariogrupo__id_grupo=grupo)
