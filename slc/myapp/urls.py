from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.novalista, name='novalista'),
    path('auth/cadastro', views.cadastro, name='cadastro'),
    path('auth/login', views.login, name='login'),
]

