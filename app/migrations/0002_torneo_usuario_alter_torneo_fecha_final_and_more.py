# Generated by Django 4.2 on 2023-09-08 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_final',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]