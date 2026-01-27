from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    name = models.CharField(max_length=200) 

    class Meta:
        ordering = ('name',) 
        verbose_name_plural = 'Categorias' 

    def __str__(self):
        return self.name 

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='libros', on_delete=models.CASCADE)

    nombre = models.CharField(max_length=200)
    descripción = models.TextField(blank=True, null=True) 
    precio = models.FloatField() 
    imagen = models.ImageField(upload_to='libro_imagen', blank=True, null=True)  

    vendido = models.BooleanField(default=False) 
    creado_por = models.ForeignKey(User, related_name='libros', on_delete=models.CASCADE)

    creado_en = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.nombre  
