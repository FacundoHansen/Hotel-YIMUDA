# Generated by Django 2.2.6 on 2019-11-01 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Concesionaria', '0002_auto_20191101_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='usuario',
        ),
        migrations.AddField(
            model_name='reserva',
            name='apellido',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
