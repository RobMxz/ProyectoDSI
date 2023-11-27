from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Alumno, HistorialAcademico, ReporteNotas

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
        exclude = ['alumno']