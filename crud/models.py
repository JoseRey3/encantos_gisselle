from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class producto(models.Model):
    tipo_prenda = models.CharField(max_length=100)
    talla = models.CharField(max_length=4)
    color = models.CharField(max_length=12)
    material = models.TextField(blank=True)
    genero = models.CharField(max_length=12)
    precio_venta = models.FloatField(max_length=6)
    marca = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo_prenda


class empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.TextField(blank=True)
    dui = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido

