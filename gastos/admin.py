from django.contrib import admin
from .models import Gasto

class GastosAdmin(admin.ModelAdmin):
    list_display = ['concepto', 'precio', 'pagado_por']
    list_filter = ['participantes']

admin.site.register(Gasto, GastosAdmin)
