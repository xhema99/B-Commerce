from django.contrib import admin

from .models import Comunicacion, Mensaje

admin.site.register(Comunicacion)
admin.site.register(Mensaje)