# Generated by Django 3.2.7 on 2021-09-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tareas',
            options={'verbose_name': 'tarea', 'verbose_name_plural': 'tareas'},
        ),
        migrations.AddField(
            model_name='tareas',
            name='tarea_pospuesta',
            field=models.BooleanField(default=False),
        ),
    ]