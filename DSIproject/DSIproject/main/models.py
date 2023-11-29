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
        return f"{self.alumno.documento_identidad}-{self.alumno.nombre} {self.alumno.apellidos} - {self.grado_academico}"
    
class ReporteNotas(models.Model):
    alumno = models.ForeignKey(HistorialAcademico, on_delete=models.CASCADE)
    fecha_subida= models.DateField()
    prom_matematica= models.FloatField(default=0)
    prom_ciencia= models.FloatField(default=0)
    prom_lenguaje= models.FloatField(default=0)

    def __str__(self):
        return f"Reporte de Notas - {self.historial_academico.alumno.nombre} {self.historial_academico.alumno.apellidos} - {self.fecha_subida}"
    

#........................................................................................    

class Psicopedagogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Psicopedagogo_DNI = models.CharField(max_length=8, unique=True)
    Psicopedagogo_NOMBRE = models.CharField(max_length=100)
    Psicopedagogo_APELLIDOS = models.CharField(max_length=100)
    Psicopedagogo_FECHA_NACIMIENTO = models.DateField()
    Psicopedagogo_GRADO_ACADEMICO = models.CharField(max_length=20)
    Psicopedagogo_NUMERO_TELEFONICO = models.CharField(max_length=9)
    Psicopedagogo_DIRECCION = models.TextField()
    Psicopedagogo_CORREO_ELECTRONICO = models.EmailField(unique=True)    

    def __str__(self):
        return f"{self.Psicopedagogo_NOMBRE} "
    
class Docente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Docente_DNI = models.CharField(max_length=8, unique=True)
    Docente_NOMBRE = models.CharField(max_length=100)
    Docente_APELLIDOS = models.CharField(max_length=100)
    Docente_FECHA_NACIMIENTO = models.DateField()
    Docente_GRADO_ACADEMICO = models.CharField(max_length=15, choices=[('Titulado', 'Titulado'),('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')])    
    Docente_NUMERO_TELEFONICO = models.CharField(max_length=9)
    Docente_DIRECCION = models.TextField()
    Docente_CORREO_ELECTRONICO = models.EmailField(unique=True)   

    def __str__(self):
        return f"{self.Docente_NOMBRE} "

class Cita(models.Model):
    psicopedagogo = models.ForeignKey(Psicopedagogo, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.psicopedagogo.nombre} {self.psicopedagogo.apellidos} - {self.fecha}"


class Apoderado(models.Model):
    #alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    IDApoderado=models.CharField(max_length=8, unique=True)
    Nombre_A = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    NivelEducativo =models.CharField(max_length=15, choices=[('Primaria', 'Primaria'),('Secundaria', 'Secundaria'), ('Instituto', 'Instituto'),('Universidad', 'Universidad')])    
    Profesion = models.CharField(max_length=100)
    CorreoElectronico =models.EmailField(unique=True)  
    NumeroTelefono = models.CharField(max_length=9)
    def __str__(self):
        return f"{self.Apoderado.Nombre_A}-{self.Apoderado.Apellido} "


class InformacionExtracurricular1(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    FechaSubida = models.DateField()
    FrecuenciaSalidas = models.IntegerField(default=0)
    SoporteAcademico = models.CharField(max_length=2, choices=[('1', 'Si'),('0', 'No')]) 
    def __str__(self):
        return f"{self.alumno.nombre}-{self.FechaSubida} {self.FrecuenciaSalidas} - {self.SoporteAcademico}"

class CondicionSocioeconomica1(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    FechaSubida = models.DateField()
    AccesoInternet = models.CharField(max_length=2, choices=[('1', 'Si'),('0', 'No')]) 
    ZonaVivienda = models.CharField(max_length=15, choices=[('Rural', 'Rural'),('Urbano', 'Urbano')])
    TiempoViaje =  models.IntegerField(default=0)

    def __str__(self):
        return f"{self.alumno.nombre}-{self.FechaSubida}-{self.AccesoInternet}"

class Administrador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    correo_electronico = models.EmailField(unique=True)
    Nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

