# Generated by Django 5.1.2 on 2024-10-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_alter_pedido_fecha_emision'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiaprima',
            name='cantidadMinima',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
