from django.contrib import admin
from .models import Tareas

# Register your models here.
class TareasAdmin(admin.ModelAdmin):
    list_display = ['nombre_tareas', 'fecha_limite', 'es_periodica']

admin.site.register(Tareas, TareasAdmin)