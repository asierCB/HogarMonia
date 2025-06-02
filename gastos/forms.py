from django import forms

from core.models import UsuarioGrupo
from .models import Gasto
from django.contrib.auth.models import User

class GastoForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(
        queryset=UsuarioGrupo.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'custom-checkbox',
            'style': 'display: flex; flex-direction: column; gap: 8px;'
            #'style': 'display: flex; flex-direction: column;'
        }),
        required=False
    )
    '''pagado_por = forms.ModelChoiceField(
        queryset=UsuarioGrupo.objects.none(),
        widget=forms.RadioSelect(attrs={
            'class': 'custom-radio',
            'style': 'display: flex; flex-direction: row;'
        }),
        required=True
    )'''

    class Meta:
        model = Gasto
        fields = ['concepto', 'precio', 'pagado_por', 'recurrente', 'participantes']  # Campos del formulario

    def __init__(self, *args, **kwargs):
        grupo = kwargs.pop('grupo', None)  # sacamos el grupo del constructor
        super().__init__(*args, **kwargs)
        if grupo:
            # Solo mostramos los usuarios que pertenecen al grupo
            self.fields['participantes'].queryset = UsuarioGrupo.objects.filter(grupo=grupo)#usuariogrupo__id_grupo=grupo)
            self.fields['pagado_por'].queryset = UsuarioGrupo.objects.filter(grupo=grupo)
