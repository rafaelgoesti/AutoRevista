# Generated by Django 5.1.6 on 2025-03-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0011_alter_carros_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='valor',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
    ]
