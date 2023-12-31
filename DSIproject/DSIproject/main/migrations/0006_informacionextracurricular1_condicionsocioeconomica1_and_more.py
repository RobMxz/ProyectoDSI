# Generated by Django 4.2.7 on 2023-11-29 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_remove_docente_docente_contrasena_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionExtracurricular1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaSubida', models.DateField()),
                ('FrecuenciaSalidas', models.IntegerField(default=0)),
                ('SoporteAcademico', models.CharField(choices=[('1', 'Si'), ('0', 'No')], max_length=2)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='CondicionSocioeconomica1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaSubida', models.DateField()),
                ('AccesoInternet', models.CharField(choices=[('1', 'Si'), ('0', 'No')], max_length=2)),
                ('ZonaVivienda', models.CharField(choices=[('Rural', 'Rural'), ('Urbano', 'Urbano')], max_length=15)),
                ('TiempoViaje', models.IntegerField(default=0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identidad', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('Nacimiento', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
