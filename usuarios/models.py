from django.db import models

class Usuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('usuario', 'Usuario'),
    )

    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )

    nombre_completo = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')

    def __str__(self):
        return f"{self.nombre_completo} ({self.rol})"

    class Meta:
        verbose_name_plural = "Usuarios"
