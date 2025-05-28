from django import forms
from core.models import *
from .models import *
from django.contrib.auth.models import User

class ListaCompraForm(forms.ModelForm):
    class Meta:
        model = ListaCompra
        fields = ['nombre_lista']
        widgets = {
            'nombre_lista': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la lista'
            })
        }

class ProductoListaForm(forms.ModelForm):
    # Campo personalizado para las opciones tipo con checkboxes
    tipos_seleccionados = forms.MultipleChoiceField(
        choices=ProductoLista.TIPOS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tipos'
    )

    class Meta:
        model = ProductoLista
        fields = ['nombre_producto', 'cantidad', 'unidades', 'id_lista']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.1',
                'style': 'width: 50px'
            }),
            'unidades': forms.Select(attrs={'class': 'form-control'}),
            'id_lista': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        grupo = kwargs.pop('grupo', None)
        super().__init__(*args, **kwargs)

        # Filtrar las listas disponibles por grupo
        if grupo:
            self.fields['id_lista'].queryset = ListaCompra.objects.filter(
                id_grupo=grupo,
                activa=True
            )
            self.fields['id_lista'].empty_label = "Selecciona una lista"

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Procesar los tipos seleccionados (si necesitas guardar múltiples tipos)
        tipos = self.cleaned_data.get('tipos_seleccionados')
        if tipos:
            # Si solo quieres guardar el primero seleccionado
            instance.tipo = tipos[0] if tipos else ''

        if commit:
            instance.save()
        return instance


