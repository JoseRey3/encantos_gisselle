# Generated by Django 4.2.6 on 2023-10-17 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_alter_producto_precio_compra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_categoria',
            new_name='nom_categoria',
        ),
    ]