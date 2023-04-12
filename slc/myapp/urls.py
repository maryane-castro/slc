from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.novalista, name='novalista'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
]