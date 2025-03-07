# Generated by Django 5.1.6 on 2025-03-05 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0006_rename_imagens_carousel_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='carros',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carros.marca'),
        ),
    ]
