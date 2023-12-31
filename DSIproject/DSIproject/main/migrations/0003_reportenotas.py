# Generated by Django 4.2.6 on 2023-11-27 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_historialacademico'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteNotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_subida', models.DateField()),
                ('prom_matematica', models.FloatField(default=0)),
                ('prom_ciencia', models.FloatField(default=0)),
                ('prom_lenguaje', models.FloatField(default=0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.historialacademico')),
            ],
        ),
    ]
