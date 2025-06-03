from django.db import models
from django.contrib.auth.models import User
import uuid

class GrupoHogar(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=50, null=False, blank=False)
    codigo_invitacion = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper())
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_grupo

    class Meta:
        verbose_name = "Grupo del Hogar"
        verbose_name_plural = "Grupos del Hogar"


class UsuarioGrupo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoHogar, on_delete=models.CASCADE)
    fecha_union = models.DateField(auto_now_add=True)
    rol = models.CharField(max_length=20, default='Miembro')

    def __str__(self):
        return f"{self.usuario.username}"# en {self.grupo.nombre_grupo}"

    class Meta:
        verbose_name = "Usuario en Grupo"
        verbose_name_plural = "Usuarios en Grupos"