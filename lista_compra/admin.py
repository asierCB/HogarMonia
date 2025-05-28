from django.contrib import admin
from .models import ListaCompra, ProductoLista

class ListaCompraAdmin(admin.ModelAdmin):
    list_display = ['id_lista', 'nombre_lista']

class ProductoListaAdmin(admin.ModelAdmin):
    list_display = ['id_lista', 'id_producto', 'nombre_producto', 'cantidad', 'comprado', 'tipo']
    list_filter = ['id_lista']

admin.site.register(ListaCompra, ListaCompraAdmin)
admin.site.register(ProductoLista, ProductoListaAdmin)
