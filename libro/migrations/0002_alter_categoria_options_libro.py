import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categorias'},
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripción', models.TextField(blank=True, null=True)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='libro_imagen')),
                ('stock', models.BooleanField(default=False)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='libro.categoria')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
