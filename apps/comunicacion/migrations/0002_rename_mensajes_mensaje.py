from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mensajes',
            new_name='Mensaje',
        ),
    ]
