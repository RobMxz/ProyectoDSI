# Generated by Django 4.2.7 on 2023-11-28 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_reportenotas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psicopedagogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Psicopedagogo_DNI', models.CharField(max_length=8, unique=True)),
                ('Psicopedagogo_NOMBRE', models.CharField(max_length=100)),
                ('Psicopedagogo_APELLIDOS', models.CharField(max_length=100)),
                ('Psicopedagogo_FECHA_NACIMIENTO', models.DateField()),
                ('Psicopedagogo_GRADO_ACADEMICO', models.CharField(max_length=20)),
                ('Psicopedagogo_NUMERO_TELEFONICO', models.CharField(max_length=9)),
                ('Psicopedagogo_DIRECCION', models.TextField()),
                ('Psicopedagogo_CORREO_ELECTRONICO', models.EmailField(max_length=254, unique=True)),
                ('Psicopedagogo_CONTRASENA', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Docente_DNI', models.CharField(max_length=8, unique=True)),
                ('Docente_NOMBRE', models.CharField(max_length=100)),
                ('Docente_APELLIDOS', models.CharField(max_length=100)),
                ('Docente_FECHA_NACIMIENTO', models.DateField()),
                ('Docente_GRADO_ACADEMICO', models.CharField(choices=[('Titulado', 'Titulado'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=15)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('Docente_NUMERO_TELEFONICO', models.CharField(max_length=9)),
                ('Docente_DIRECCION', models.TextField()),
                ('Docente_CORREO_ELECTRONICO', models.EmailField(max_length=254, unique=True)),
                ('Docente_CONTRASENA', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
