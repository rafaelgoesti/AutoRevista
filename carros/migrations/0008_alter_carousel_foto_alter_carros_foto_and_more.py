# Generated by Django 5.1.6 on 2025-03-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0007_marca_alter_carros_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='foto',
            field=models.ImageField(upload_to='carousel'),
        ),
        migrations.AlterField(
            model_name='carros',
            name='foto',
            field=models.ImageField(upload_to='carros'),
        ),
        migrations.AlterField(
            model_name='carros',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
