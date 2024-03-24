# Generated by Django 5.0.3 on 2024-03-22 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=70, verbose_name='Nombre del Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Producto')),
                ('nombreProducto', models.CharField(max_length=80, verbose_name='Nombre del producto')),
                ('valorProducto', models.IntegerField(verbose_name='Valor de Producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]