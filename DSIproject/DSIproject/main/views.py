from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm,AlumnoForm, HistorialAcademicoForm, ReporteNotasForm, PsicopedagogoForm, DocenteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import Alumno, HistorialAcademico, ReporteNotas, Psicopedagogo, Docente
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
            return redirect("/home")
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
            return redirect("/home")
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
            return redirect("/home")
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
            return redirect("/home")
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
    return render(request,'main/estudiante.html', context)

def psicopedagogo(request):
    return render(request,'main/psico.html')


#........................................................................................  

def create_psicopedagogo(request):
    if request.method == 'POST':
        form = PsicopedagogoForm(request.POST)
        if form.is_valid():
            psicopedagogo = form.save(commit=False)
            psicopedagogo.user = request.user
            psicopedagogo.save()
            return redirect("/home")
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