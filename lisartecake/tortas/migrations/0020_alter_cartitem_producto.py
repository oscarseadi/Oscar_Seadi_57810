# Generated by Django 5.0.6 on 2024-07-20 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortas', '0019_alter_cartitem_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tortas.torta'),
        ),
    ]
