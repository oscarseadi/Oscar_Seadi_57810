# Generated by Django 5.0.6 on 2024-06-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('dimensiones', models.CharField(max_length=50)),
                ('misc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Torta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('cubierta', models.CharField(max_length=200)),
                ('relleno', models.CharField(max_length=250)),
                ('cantidad_personas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TortaP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('cubierta', models.CharField(max_length=200)),
                ('relleno', models.CharField(max_length=250)),
                ('cantidad_personas', models.IntegerField()),
                ('motivo', models.CharField(max_length=100)),
                ('agregados', models.IntegerField()),
            ],
        ),
    ]
