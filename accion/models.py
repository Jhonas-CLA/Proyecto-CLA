from django.db import models

class Interfaz(models.Model):
    interfaz=models.CharField(max_length=100)
    def _str_(self):
        return self.interfaz
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    calificacion = models.IntegerField(default=0)

def get_precio_formateado(self):
    return "${:,.0f}".format(self.precio)

def get_precio_anterior_formateado(self):
    return "${:,.0f}".format(self.precio_anterior)  # si existe ese campo

def get_stars_display(self):
    estrellas = '★' * self.calificacion + '☆' * (5 - self.calificacion)
    return estrellas

    @property
    def imagen_url(self):
        if self.imagen:
            return self.imagen.url
        return ""
    

#Administrador

class Administrador(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True, null=True)
    nombre_negocio = models.CharField(max_length=100)
    nit_rut = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_completo
    
#Proveedor

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    contacto = models.EmailField()
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre

# Create your models here.