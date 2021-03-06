# Generated by Django 3.2.7 on 2021-10-02 14:24

from django.db import migrations, models
import django.db.models.deletion
import tareas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField(max_length=5000)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=tareas.models.path_to_tareas)),
                ('tarea_activa', models.BooleanField(default=False)),
                ('tarea_pospuesta', models.BooleanField(default=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categorias')),
            ],
            options={
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
            },
        ),
    ]
