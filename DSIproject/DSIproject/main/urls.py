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
    path('editar-alumno',views.editar_alumno, name='editar_alumno'),
    path('create-historial',views.create_historial, name='create_historial'),
    path('editar-historial',views.editar_historial, name='editar_historial'),
    path('create-notas',views.create_notas, name='create_notas'),
    path('estudiante-notas',views.estudiante_notas, name='estudiante_notas'),
    path('create-psicopedagogo',views.create_psicopedagogo, name='create_psicopedagogo'),
    path('create-docente',views.create_docente, name='create_docente'),
    path('docente',views.docente, name='docente'),
    path('editar-docente',views.editar_docente, name='editar_docente'),
    path('editar-psicopedagogo',views.editar_psicopedagogo, name='editar_psicopedagogo'),
    path('create-cita',views.create_cita, name='create_cita'),
]
