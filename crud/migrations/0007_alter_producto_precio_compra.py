# Generated by Django 4.2.6 on 2023-10-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_alter_producto_precio_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_compra',
            field=models.FloatField(blank=True, default=0, max_length=6, null=True),
        ),
    ]