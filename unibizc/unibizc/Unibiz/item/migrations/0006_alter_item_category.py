# Generated by Django 4.2.7 on 2023-11-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.IntegerField(choices=[(1, 'Detalles'), (0, 'Alimentos Dulces'), (2, 'Mecatos'), (4, 'Utensilios'), (3, 'Miscelanea')]),
        ),
    ]
