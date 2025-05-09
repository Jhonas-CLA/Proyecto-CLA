from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    gmail = models.EmailField()
    telefono = models.CharField(max_length=20)
    dependencia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo


# Create your models here.
