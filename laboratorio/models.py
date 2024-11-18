from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.laboratorio
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    p_costo = models.FloatField(blank=False, null=False,)
    p_venta = models.FloatField(blank=False, null=False,)
    
    def __str__(self):
        return self.nombre
