from datetime import datetime, timedelta
from django.db.models import Q
from .models import Tareas
from django.utils import timezone


def del_tareas():
    """
    Elimina tareas completadas o caducadas
    """
    tareas_a_eliminar = Tareas.objects.filter(
        Q(fecha_limite__lt=timezone.now()) | Q(completada=True)
    )

    count = tareas_a_eliminar.count()
    tareas_a_eliminar.delete()

    return count


def duplicar_tarea():
    """
    Duplica solo las tareas periódicas que han caducado o están completadas
    """
    tareas = Tareas.objects.filter(
        es_periodica=True
    ).filter(
        Q(fecha_limite__lt=timezone.now()) | Q(completada=True)
    )

    count = 0
    for tarea in tareas:
        # Crear nueva tarea
        tarea.pk = None
        tarea.id = None
        tarea.fecha_limite = tarea.fecha_limite + timedelta(days=7)

        # Resetear estado de completada para la nueva tarea
        tarea.completada = False

        tarea.save()
        count += 1

    return count
