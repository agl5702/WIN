# Generated by Django 4.2 on 2023-09-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('deporte', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_final', models.DateField(default='2023-12-31')),
            ],
        ),
    ]
