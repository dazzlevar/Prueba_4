# Generated by Django 4.0.5 on 2022-07-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_descuentoproducto_descuentocategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('standard', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
            ],
        ),
    ]
