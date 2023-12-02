from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Alumno, Administrador, HistorialAcademico, ReporteNotas, Psicopedagogo, Cita, Docente, InformacionExtracurricular1,Apoderado,CondicionSocioeconomica1


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        exclude="__all__"   
    
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

 #gaa---------------------------------- 

class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado     
        fields = "__all__"      

class CondicionSocioeconomicaForm(forms.ModelForm):
    class Meta:
        model = CondicionSocioeconomica1
        fields = "__all__"  
class InformacionExtracurricularForm(forms.ModelForm):
    class Meta:
        model = InformacionExtracurricular1
        fields = "__all__"  

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = "__all__"   
