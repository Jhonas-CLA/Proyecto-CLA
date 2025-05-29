from django.db import models

class Interfaz(models.Model):
    interfaz=models.CharField(max_length=100)
    def __str__(self):
        return self.interfaz
    

# Create your models here.


