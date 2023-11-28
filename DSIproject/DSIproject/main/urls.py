from django.urls import path
from . import views
from .views import redirection_view

urlpatterns =[
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('redirection/', redirection_view, name='redirection_view'),
    path('estudiante',views.estudiante, name='estudiante'),
    path('psicopedagogo',views.psicopedagogo, name='psico'),
    path('create-alumno', views.create_alumno, name='create_alumno'),
    path('editar_alumno',views.editar_alumno, name='editar_alumno'),
    path('create-historial',views.create_historial, name='create_historial'),
    path('editar_historial',views.editar_historial, name='editar_historial'),
    path('create_notas',views.create_notas, name='create_notas'),
    path('estudiante_notas',views.estudiante_notas, name='estudiante_notas'),
]
