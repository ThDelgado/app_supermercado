from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)  
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    precio = models.PositiveIntegerField(blank=False, null=False, default=999999)
   
    class Meta:
        db_table = 'Productos'
        
    def __str__(self):   
        return self.nombre