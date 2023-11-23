from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __srt__(self):
        return self.nombre_categoria 
    
opciones_genero = [
    [0, "Mujer"],
    [1, "Hombre"],
    [2, "Niños"],
]
    
class producto(models.Model):
    tipo_prenda = models.CharField(max_length=100)
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=50, blank=True)
    material = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    nombre_categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)
    genero = models.IntegerField(choices=opciones_genero)
    marca = models.CharField(max_length=50, blank=True)
    precio_compra = models.FloatField(max_length=6, null=True, blank=True, default=0)
    precio_venta = models.FloatField(max_length=6, null=True, blank=True, default=0)
    existencias = models.IntegerField(null=True, blank=True, default=0) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.tipo_prenda
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        

class empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.TextField(blank=True)
    dui = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class compra(models.Model):
    numero_compra = models.IntegerField()
    fecha_compra = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __srt__(self):
        return self.numero_compra + ' ' + self.fecha_creacion

class detalle_compra(models.Model):
    tipo_prenda = models.ForeignKey(producto, on_delete=models.CASCADE)
    precio_compra = models.FloatField(max_length=6, null=True, blank=True, default=0)
    cantidad = models.IntegerField(default=0)
    subtotal= models.FloatField(max_length=6, null=True, blank=True, default=0)
    numero_compra = models.ForeignKey(compra, on_delete=models.CASCADE)
    
    def __srt__(self):
        return self.tipo_prenda 
    