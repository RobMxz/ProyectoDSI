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
]
