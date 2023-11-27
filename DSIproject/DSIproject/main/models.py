from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alumno(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class HistorialAcademico(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    grado_academico = models.CharField(max_length=50)
    numero_repitencias = models.IntegerField(default=0)
    tiempo_estudio = models.IntegerField()  # Puedes ajustar este campo según tus necesidades
    preferencia_profesional = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.alumno.nombre} {self.alumno.apellidos} - {self.grado_academico}"
    
class ReporteNotas(models.Model):
    alumno = models.ForeignKey(HistorialAcademico, on_delete=models.CASCADE)
    fecha_subida= models.DateField()
    prom_matematica= models.FloatField(default=0)
    prom_ciencia= models.FloatField(default=0)
    prom_lenguaje= models.FloatField(default=0)

    def __str__(self):
        return f"Reporte de Notas - {self.historial_academico.alumno.nombre} {self.historial_academico.alumno.apellidos} - {self.fecha_subida}"
    