from django.db import models
class Interfaz(models.Model):
    interfaz=models.CharField(max_length=100)
    def __str__(self):
        return self.interfaz
    

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=255)
    gmail = models.EmailField()
    telefono = models.CharField(max_length=20)
    dependencia = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre_completo

# Create your models here.


