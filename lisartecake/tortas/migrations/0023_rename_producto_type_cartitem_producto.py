# Generated by Django 5.0.6 on 2024-07-20 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tortas', '0022_alter_cartitem_producto_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='producto_type',
            new_name='producto',
        ),
    ]
