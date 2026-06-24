import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0003_rename_stock_libro_vendido'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('modificado_en', models.DateTimeField(auto_now=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversaciones', to='libro.libro')),
                ('miembros', models.ManyToManyField(related_name='conversaciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modificado_en',),
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='comunicacion.comunicacion')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensaje_creado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
