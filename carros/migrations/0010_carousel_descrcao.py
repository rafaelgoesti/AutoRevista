# Generated by Django 5.1.6 on 2025-03-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0009_alter_carros_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='descrcao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
