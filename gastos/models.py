#models.py

from django.db import models
from core.models import *
from django.contrib.auth.models import User

# Create your models here.

class Gasto(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_gasto = models.DateField(auto_now_add=True)
    pagado_por = models.ForeignKey(UsuarioGrupo, blank=True, null=True, on_delete=models.SET_NULL)
    recurrente = models.BooleanField(default=False)
    participantes = models.ManyToManyField(UsuarioGrupo, related_name='gastos')
    grupo = models.ForeignKey(GrupoHogar, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.concepto

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
