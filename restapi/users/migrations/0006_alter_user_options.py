# Generated by Django 3.2.7 on 2021-09-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
    ]