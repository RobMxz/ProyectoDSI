from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm,AlumnoForm, HistorialAcademicoForm, ReporteNotasForm, PsicopedagogoForm, DocenteForm, CitaForm,ApoderadoForm,CondicionSocioeconomicaForm,InformacionExtracurricularForm,AdministradorForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import Alumno, HistorialAcademico, ReporteNotas, Psicopedagogo, Docente, Cita, Apoderado,InformacionExtracurricular1,CondicionSocioeconomica1,Administrador
import subprocess
# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def create_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.user = request.user
            alumno.save()
            return redirect("/estudiante")
    else:
        form = AlumnoForm()

    return render(request, 'main/create_alumno.html', {'form': form})

@login_required(login_url="/login")
def editar_alumno(request):
    alumno = get_object_or_404(Alumno, user=request.user)

    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = AlumnoForm(instance=alumno)

    return render(request, 'main/editar_alumno.html', {'form': form})

@login_required(login_url="/login")
def create_historial(request):
    alumno = get_object_or_404(Alumno, user=request.user)
    if request.method == 'POST':
        form = HistorialAcademicoForm(request.POST)
        if form.is_valid():
            historial_academico = form.save(commit=False)
            historial_academico.alumno = alumno
            historial_academico.save()
            return redirect("/estudiante")
    else:
        form = HistorialAcademicoForm()

    return render(request, 'main/create_historial.html', {'form': form})

@login_required(login_url="/login")
def editar_historial(request):
    user_actual = request.user
    alumnos = Alumno.objects.filter(user=user_actual)
    alumno = get_object_or_404(Alumno, user=request.user)
    hist = get_object_or_404(HistorialAcademico, alumno=alumno)

    if request.method == 'POST':
        form = HistorialAcademicoForm(request.POST, instance=hist)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = HistorialAcademicoForm(instance=hist)

    return render(request, 'main/editar_historial.html', {'form': form})

@login_required(login_url="/login")
def create_notas(request):

    if request.method == 'POST':
        form = ReporteNotasForm(request.POST)
        if form.is_valid():
            user_actual = request.user
            alumnos = Alumno.objects.filter(user=user_actual)
            alumno = get_object_or_404(Alumno, user=request.user)
            hist = get_object_or_404(HistorialAcademico, alumno=alumno)
            nota = form.save(commit=False)
            nota.alumno = hist
            nota.save()
            return redirect("/docente")
    else:
        form = ReporteNotasForm()

    return render(request, 'main/create_notas.html', {'form': form})


@login_required(login_url="/login")
def create_notas(request):
    if request.method == 'POST':
        form = ReporteNotasForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.save()
<<<<<<< HEAD
            return redirect("/docente")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = ReporteNotasForm()

    # Obtén todos los historiales académicos para mostrar en el desplegable del formulario
    historiales_academicos = HistorialAcademico.objects.all()

    return render(request, 'main/create_notas.html', {'form': form, 'historiales_academicos': historiales_academicos})



@login_required(login_url="/login")
def estudiante_notas(request):
    user_actual = request.user
    alumnos = Alumno.objects.filter(user=user_actual)
    alumno = get_object_or_404(Alumno, user=request.user)
    hists = HistorialAcademico.objects.filter(alumno=alumno)
    hist = hists[0]
    notas = ReporteNotas.objects.filter(alumno=hist)
    
    return render(request,'main/estudiante_notas.html', {'notas':notas})
    

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form":form})

    path('sign-up', views.sign_up, name='sign_up'),

def redirection_view(request):
    # Obtén el grupo del usuario actual
    user_group = request.user.groups.first()
    # Determina la URL de redirección según el grupo
    if user_group and user_group.name == 'Estudiante':
        return redirect('/estudiante')
    elif user_group and user_group.name == 'Psicopedagogo':
        return redirect('/psicopedagogo')
    elif user_group and user_group.name == 'Docente':
        return redirect('/docente')
<<<<<<< HEAD
    elif user_group and user_group.name == 'Administrador':
        return redirect('/administrador')
=======
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    elif request.user.is_superuser:
        return redirect('/admin')
    else:
        # Redirección por defecto si el grupo no coincide con ninguno de los anteriores
        return redirect('/home')

def estudiante(request):
    user_actual = request.user
    alumnos = Alumno.objects.filter(user=user_actual)
    alumno = get_object_or_404(Alumno, user=request.user)
    hists = HistorialAcademico.objects.filter(alumno=alumno)
    context = {"alumnos": alumnos, "hists": hists}
    citas = Cita.objects.filter(alumno=alumno)
    context = {"alumnos": alumnos, "hists": hists, "citas":citas}
    return render(request,'main/estudiante.html', context)

def psicopedagogo(request):
    user_actual = request.user
    psicopedagogos = Psicopedagogo.objects.filter(user=user_actual)
    context = {"psicopedagogos": psicopedagogos}
    return render(request,'main/psico.html', context)


#........................................................................................  

def create_psicopedagogo(request):
    if request.method == 'POST':
        form = PsicopedagogoForm(request.POST)
        if form.is_valid():
            psicopedagogo = form.save(commit=False)
            psicopedagogo.user = request.user
            psicopedagogo.save()
<<<<<<< HEAD
            return redirect("/psicopedagogo")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = PsicopedagogoForm()

    return render(request, 'main/create_psicopedagogo.html', {'form': form})


def create_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            docente = form.save(commit=False)
            docente.user = request.user
            docente.save()
            return redirect("/home")
    else:
        form = DocenteForm()

    return render(request, 'main/create_docente.html', {'form': form})

def docente(request):
    user_actual = request.user
    docentes = Docente.objects.filter(user=user_actual)
    context = {"docentes": docentes}
    return render(request,'main/docente.html', context)

@login_required(login_url="/login")
def editar_docente(request):
    docente = get_object_or_404(Docente, user=request.user)

    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = DocenteForm(instance=docente)

    return render(request, 'main/editar_docente.html', {'form': form})

@login_required(login_url="/login")
def editar_psicopedagogo(request):
    psicopedagogo = get_object_or_404(Psicopedagogo, user=request.user)

    if request.method == 'POST':
        form = PsicopedagogoForm(request.POST, instance=psicopedagogo)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            return redirect("/psicopedagogo")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = PsicopedagogoForm(instance=psicopedagogo)

    return render(request, 'main/editar_psicopedagogo.html', {'form': form})

@login_required(login_url="/login")
def create_cita(request):
    #psicopedagogo = get_object_or_404(Psicopedagogo, user=request.user)
    #BORRAR psicopedgagog
    psicopedagogo = Psicopedagogo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.psicopedagogo = psicopedagogo
            cita.save()
            username = cita.alumno.nombre
            dni = cita.alumno.documento_identidad
            #promM = str(promedioN1(cita.alumno.id))
            a = promedioN1(cita.alumno.id)
            promM = str(a)
            b = promedioN3(cita.alumno.id)
            promL = str(b)
            c = promedioN2(cita.alumno.id)
            promC = str(c)
            
            nac=str(cita.alumno.fecha_nacimiento)
            
            b = HistorialAcademico.objects.get(alumno=cita.alumno)
            tmp_est = str(b.tiempo_estudio)
            failures =str(b.numero_repitencias)
            higher = b.preferencia_profesional 
<<<<<<< HEAD

            condsoc = CondicionSocioeconomica1.objects.get(alumno=cita.alumno)

            vivienda = condsoc.ZonaVivienda
            
            infEx = InformacionExtracurricular1.objects.get(alumno=cita.alumno)
            fecS = str(infEx.FrecuenciaSalidas)
            supAc = infEx.SoporteAcademico

            #print(f'EL USUARIO ES : {cita.alumno.user}')
            #apoderado = Apoderado.objects.get(user=cita.alumno.user)
            #fedu = str(apoderado.NivelEducativo)
            #profesion = apoderado.Profesion
            fedu = "Secundaria"
            profesion = "Ingeniero"


            subprocess.run(['python', 'correo.py', username,
                            dni, promM, promL, promC, nac,tmp_est,failures,higher,
                            vivienda,fecS,supAc,fedu,profesion])
            return redirect("/psicopedagogo")
=======
            subprocess.run(['python', 'correo.py', username,
                            dni, promM, promL, promC, nac,tmp_est,failures,higher])
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = CitaForm()

    return render(request, 'main/create_cita.html', {'form': form})


def promedioN1(idalumno):
    promedio =0
    alumno = Alumno.objects.get(pk=idalumno)
    b = HistorialAcademico.objects.get(alumno=alumno)
    reportes = ReporteNotas.objects.filter(alumno = b)
    
    for reporte in reportes:
        
        promedio += reporte.prom_matematica
    
    return promedio/len(reportes)

def promedioN2(idalumno):
    promedio =0
    alumno = Alumno.objects.get(pk=idalumno)
    b = HistorialAcademico.objects.get(alumno=alumno)
    reportes = ReporteNotas.objects.filter(alumno = b)
    
    for reporte in reportes:
        
        promedio += reporte.prom_ciencia
    
    return promedio/len(reportes)   

def promedioN3(idalumno):
    promedio =0
    alumno = Alumno.objects.get(pk=idalumno)
    b = HistorialAcademico.objects.get(alumno=alumno)
    reportes = ReporteNotas.objects.filter(alumno = b)
    
    for reporte in reportes:
        
        promedio += reporte.prom_lenguaje
    
    return promedio/len(reportes)

def apoderado(request):
    user_actual = request.user
    apoderados = Apoderado.objects.filter(user=user_actual)
    context = {"apoderados": apoderados}
    return render(request,'main/apoderado.html', context)

@login_required(login_url="/login")
def  create_apoderado(request):
    if request.method == 'POST':
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            apoderado = form.save(commit=False)
            apoderado.user = request.user
            apoderado.save()
<<<<<<< HEAD
            return redirect("/administrador")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = ApoderadoForm()
    return render(request, 'main/create_apoderado.html', {'form': form})


def InformacionExtracurricular(request):
    user_actual = request.user
    informaciones = InformacionExtracurricular1.objects.filter(user=user_actual)
    context = {"informaciones": informaciones}
    return render(request,'main/InformacionExtracurricular.html', context)

@login_required(login_url="/login")
def  create_InformacionExtracurricular(request):
    if request.method == 'POST':
        form = InformacionExtracurricularForm(request.POST)
        if form.is_valid():
            infor = form.save(commit=False)
            infor.user = request.user
            infor.save()
<<<<<<< HEAD
            return redirect("/administrador")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = InformacionExtracurricularForm()
    return render(request, 'main/create_InformacionExtracurricular.html', {'form': form})

def CondicionSocioeconomica(request):
    user_actual = request.user
    condiciones= CondicionSocioeconomica1.objects.filter(alumno=user_actual)
    context = {"condiciones": condiciones}
    return render(request,'main/CondicionSocioeconomica.html', context)


@login_required(login_url="/login")
def  create_CondicionSocioeconomica(request):
    if request.method == 'POST':
        form = CondicionSocioeconomicaForm(request.POST)
        if form.is_valid():
            cond = form.save(commit=False)
            cond.user = request.user
            cond.save()
<<<<<<< HEAD
            return redirect("/administrador")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = CondicionSocioeconomicaForm()
    return render(request, 'main/create_CondicionSocioeconomica.html', {'form': form})

def administrador(request):
    user_actual = request.user
    administradores = Administrador.objects.filter(user=user_actual)
    context = {"administradores": administradores}
    return render(request,'main/administrador.html', context)


@login_required(login_url="/login")
def  create_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            adm = form.save(commit=False)
            adm.user = request.user
            adm.save()
<<<<<<< HEAD
            return redirect("/administrador")
=======
            return redirect("/home")
>>>>>>> 30f5fe3b7f257de9bafe68e0d8cfed66695bb91f
    else:
        form = AdministradorForm()

    return render(request, 'main/create_administrador.html', {'form': form})