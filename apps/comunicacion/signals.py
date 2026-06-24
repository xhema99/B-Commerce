import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Mensaje

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Mensaje)
def mensaje_enviado(sender, instance, created, **kwargs):
    if created:
        logger.info(
            "Nuevo mensaje en conversación %s de %s",
            instance.comunicacion_id,
            instance.creado_por.username,
        )
