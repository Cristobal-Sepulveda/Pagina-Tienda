# Generated by Django 3.2.12 on 2022-06-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del Producto')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('descripcion', models.CharField(max_length=40, verbose_name='Descripcion')),
            ],
        ),
    ]
