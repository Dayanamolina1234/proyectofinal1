# Generated by Django 4.2.6 on 2023-11-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.IntegerField(choices=[(1, 'Detalles'), (0, 'Alimentos Dulces'), (2, 'Mecatos'), (4, 'Utencilios'), (3, 'Miscelania')]),
        ),
    ]
