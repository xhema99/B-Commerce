from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_categoria_options_libro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='stock',
            new_name='vendido',
        ),
    ]
