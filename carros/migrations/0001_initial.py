# Generated by Django 5.1.6 on 2025-03-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('valor', models.FloatField(default=0.0)),
                ('descrição', models.TextField()),
            ],
        ),
    ]
