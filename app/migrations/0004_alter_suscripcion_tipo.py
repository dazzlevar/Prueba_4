# Generated by Django 4.0.4 on 2022-06-29 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tipo_sub_suscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_sub'),
        ),
    ]
