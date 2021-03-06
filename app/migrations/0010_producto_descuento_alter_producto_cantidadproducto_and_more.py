# Generated by Django 4.0.4 on 2022-07-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_datos_cupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.IntegerField(null=True, verbose_name=' Descuento '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidadProducto',
            field=models.IntegerField(null=True, verbose_name=' Cantidad '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionProducto',
            field=models.TextField(verbose_name=' Descripcion del producto '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to=' productos '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=50, verbose_name=' Nombre del Producto '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precioProducto',
            field=models.IntegerField(verbose_name=' Precio del producto '),
        ),
    ]
