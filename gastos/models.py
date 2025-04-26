from django.db import models
from core.models import *
from django.contrib.auth.models import User

# Create your models here.

class Gasto(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_gasto = models.DateField(auto_now_add=True)
    pagado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.concepto

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
