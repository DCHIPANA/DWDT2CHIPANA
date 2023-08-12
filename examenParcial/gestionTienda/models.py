from django.db import models

# Create your models here.

class infoTienda(models.Model):
    Direccion = models.CharField(max_length=32, blank=True, null=True)
    Provincia = models.CharField(max_length=32, blank=True, null=True)
    Region = models.CharField(max_length=32, blank=True, null=True)
    Fecha_creacion = models.CharField(max_length=32, blank=True, null=True)
    Telefono_contacto = models.CharField(max_length=32, blank=True, null=True)

class infoProducto(models.Model):
    Codigo = models.CharField(max_length=32, blank=True, null=True)
    Descripcion = models.CharField(max_length=32, blank=True, null=True)
    Precio_venta = models.CharField(max_length=32, blank=True, null=True)
    Cantidad = models.CharField(max_length=32, blank=True, null=True)
    Tienda_relacionada = models.OneToOneField(infoTienda, on_delete=models.SET_NULL, null=True, blank=True)