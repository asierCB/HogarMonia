from datetime import datetime
from .models import Tareas

def del_tareas():
    tareas = Tareas.objects.all()#.filter(completada=True)
    for tarea in tareas:
        if tarea.fecha_limite < datetime.now() or tarea.completada:
            tarea.delete()