# productos/models.py

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=15, decimal_places=0)

    def _str_(self):
        return self.nombre