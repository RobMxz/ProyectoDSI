from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

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
    elif request.user.is_superuser:
        return redirect('/admin')
    else:
        # Redirección por defecto si el grupo no coincide con ninguno de los anteriores
        return redirect('/home')

def estudiante(request):
    return render(request,'main/estudiante.html')

def psicopedagogo(request):
    return render(request,'main/psico.html')