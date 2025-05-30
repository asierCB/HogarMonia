from datetime import datetime, timedelta
from .models import Tareas

def del_tareas():
    tareas = Tareas.objects.all()#.filter(completada=True)
    for tarea in tareas:
        if tarea.fecha_limite < datetime.now() or tarea.completada:
            tarea.delete()

def duplicar_tarea():
    tareas = Tareas.objects.all().filter(es_periodica=True)
    for tarea in tareas:
        tarea.pk = None
        tarea.id = None
        tarea.fecha_limite = tarea.fecha_limite + timedelta(days=7)
        tarea.save()