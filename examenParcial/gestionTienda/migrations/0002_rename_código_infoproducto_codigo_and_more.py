# Generated by Django 4.2.3 on 2023-08-12 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoproducto',
            old_name='Código',
            new_name='Codigo',
        ),
        migrations.RenameField(
            model_name='infoproducto',
            old_name='Descripción',
            new_name='Descripcion',
        ),
    ]
