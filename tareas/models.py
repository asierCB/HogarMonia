from django.contrib.auth.models import User
from django.db import models
from core.models import *

# Create your models here.

class Tareas(models.Model):
    id_tareas = models.AutoField(primary_key=True)
    nombre_tareas = models.CharField(max_length=50)
    fecha_limite = models.DateField(auto_now_add=False, blank=True, null=True)
    es_periodica = models.BooleanField(default=False)
    frecuencia = models.IntegerField(default=1, verbose_name='Frecuencia (Veces a la semana)')
    completada = models.BooleanField(default=False)
    tiempo_estimado = models.FloatField(default=0.5, )
    participantes = models.ForeignKey(UsuarioGrupo, related_name='tareas', blank=True, null=True, on_delete=models.SET_NULL)

    #participantes = models.ManyToManyField(UsuarioGrupo, related_name='tareas', blank=True, null=True)
    grupo = models.ForeignKey(GrupoHogar, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre_tareas

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"