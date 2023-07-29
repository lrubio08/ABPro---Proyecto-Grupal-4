from django.db import models
# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, null = True)
    email = models.CharField(max_length=50, null = True)
    telefono = models.CharField(max_length=10, null = True)
    productos = models.CharField(max_length=200, null= True)
    def __str__(self):
        return self.nombre
