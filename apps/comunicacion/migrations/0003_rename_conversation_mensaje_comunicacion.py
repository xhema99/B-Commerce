from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunicacion', '0002_rename_mensajes_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='conversation',
            new_name='comunicacion',
        ),
    ]
