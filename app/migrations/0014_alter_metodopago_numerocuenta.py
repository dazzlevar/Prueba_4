# Generated by Django 4.0.5 on 2022-07-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_metodopago_delete_banco_delete_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodopago',
            name='numeroCuenta',
            field=models.IntegerField(null=True, verbose_name='numero de cuenta'),
        ),
    ]