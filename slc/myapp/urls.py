from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('auth/cadastro', views.cadastro, name='cadastro'),
    path('auth/login', views.login, name='login'),
    path('verlistas', views.verlistas, name='verlistas'),
    path('novo', views.novalista, name='novalista'),
    path('update/<int:pk>', views.update, name='update')
    
]

