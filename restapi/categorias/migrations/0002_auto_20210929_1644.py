# Generated by Django 3.2.7 on 2021-09-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AddField(
            model_name='categorias',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
