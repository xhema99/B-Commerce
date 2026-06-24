from django.contrib.auth.models import User
from django.db import models

from libro.models import Libro

class Comunicacion(models.Model):
    libro = models.ForeignKey(Libro, related_name='conversaciones', on_delete=models.CASCADE)
    
    miembros = models.ManyToManyField(User, related_name='conversaciones')
    
    creado_en = models.DateTimeField(auto_now_add=True)
    
    modificado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modificado_en',)

class Mensaje(models.Model):
    comunicacion = models.ForeignKey(Comunicacion, related_name='mensajes', on_delete=models.CASCADE)
    
    contenido = models.TextField()
    
    creado_en = models.DateTimeField(auto_now_add=True)
    
    creado_por = models.ForeignKey(User, related_name='mensaje_creado', on_delete=models.CASCADE)
