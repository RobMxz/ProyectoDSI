from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Alumno, HistorialAcademico, ReporteNotas, Psicopedagogo, Docente, Cita

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        exclude=['user'] 
    
class HistorialAcademicoForm(forms.ModelForm):
    class Meta:
        model = HistorialAcademico
        exclude = ['alumno']
        
class ReporteNotasForm(forms.ModelForm):
    class Meta:
        model = ReporteNotas     
        fields = "__all__"   

#........................................................................................  

class PsicopedagogoForm(forms.ModelForm):
    class Meta:
        model = Psicopedagogo
        exclude=['user'] 

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        exclude=['user'] 

#------------------------------------------------------
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        exclude = ['psicopedagogo']