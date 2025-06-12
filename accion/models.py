from django.db import models
from django.contrib.auth.models import User

class Interfaz(models.Model):
    interfaz=models.CharField(max_length=100)
    def _str_(self):
        return self.interfaz
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    
    # Campos adicionales que puedes necesitar
    imagen_url = models.URLField(blank=True, null=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    es_oferta = models.BooleanField(default=False)
    es_nuevo = models.BooleanField(default=False)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tu_tabla_productos'  # Cambia por el nombre real de tu tabla
        ordering = ['-fecha_creacion']  # Ordenar por más recientes primero
    
    def _str_(self):
        return self.nombre
    
    def get_stars_display(self):
        """Retorna las estrellas como string HTML"""
        filled_stars = '★' * self.rating
        empty_stars = '☆' * (5 - self.rating)
        return filled_stars + empty_stars
    
    def get_precio_formateado(self):
        """Retorna el precio formateado con separadores de miles"""
        return f"${self.precio:,.0f}".replace(',', '.')
    
    def get_precio_anterior_formateado(self):
        """Retorna el precio anterior formateado"""
        if self.precio_anterior:
            return f"${self.precio_anterior:,.0f}".replace(',', '.')
        return None
    

# Modelo administrador

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Información personal
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    foto = models.ImageField()

    # Datos del negocio
    nombre_local = models.CharField(max_length=100)
    nit = models.CharField(max_length=30)
    direccion_local = models.CharField(max_length=255)

    # Preferencias
    notificaciones = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo

# Create your models here.