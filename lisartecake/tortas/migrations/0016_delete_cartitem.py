# Generated by Django 5.0.6 on 2024-07-20 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tortas', '0015_cartitem_precio_alter_cartitem_producto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
