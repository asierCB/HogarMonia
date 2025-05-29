from django.contrib.auth.models import User
from django.db import models

from core.models import GrupoHogar


class ListaCompra(models.Model):
    id_lista = models.AutoField(primary_key=True)
    nombre_lista = models.CharField(max_length=50)
    creada_por = models.ForeignKey(User, on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)
    id_grupo = models.ForeignKey(GrupoHogar, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_lista

class ProductoLista(models.Model):
    FRUTA_VERDURA = 'Fruta/Verdura'
    CARNE = 'Carne'
    PESCADO = 'Pescado'
    LACTEOS = 'Lacteos'
    CONGELADOS = 'Congelados'
    PRECOCINADOS = 'Precocinados'
    BEBIDAS = 'Bebidas'
    OTROS = 'Otros'
    LEGUMBRES = 'Legumbres'
    CONSERVAS = 'Conservas'
    CEREALES_PASTA = 'Cereales o Pasta'
    HARINAS = 'Harinas'
    PAN = 'Pan/Bollería'
    AZUCAR = 'Azucar'
    CAFE_INFUSIONES = 'Cafe o Infusiones'
    EMBUTIDO = 'Embutido'

    TIPOS = [
        (FRUTA_VERDURA, 'Fruta/Verdura'),
        (CARNE, 'Carne'),
        (PESCADO, 'Pescado'),
        (LACTEOS, 'Lacteos'),
        (CONGELADOS, 'Congelados'),
        (PRECOCINADOS, 'Precocinados'),
        (BEBIDAS, 'Bebidas'),
        (OTROS, 'Otros'),
        (LEGUMBRES, 'Legumbres'),
        (CONSERVAS, 'Conservas'),
        (CEREALES_PASTA, 'Cereales o Pasta'),
        (HARINAS, 'Harinas'),
        (PAN, 'Pan/Bollería'),
        (AZUCAR, 'Azucar'),
        (CAFE_INFUSIONES, 'Cafe o Infusiones'),
        (EMBUTIDO, 'Embutido'),
    ]

    UD = 'ud'
    KG = 'kg'
    BOLSAS = 'bolsas/bandeja'
    GR = 'gr'

    UNIDADES = [
        (UD, 'ud'),
        (KG, 'kg'),
        (BOLSAS, 'bolsas/bandeja'),
        (GR, 'gr'),
    ]

    id_lista = models.ForeignKey(ListaCompra, on_delete=models.CASCADE)
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=1)
    unidades = models.CharField(choices=UNIDADES, max_length=20, blank=True, null=True)
    comprado = models.BooleanField(default=False)
    tipo = models.CharField(choices=TIPOS, max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id_producto}"
