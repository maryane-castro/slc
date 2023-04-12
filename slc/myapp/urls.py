from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('auth/cadastro', views.cadastro, name='cadastro'),
    path('auth/login', views.login, name='login'),
    path('verlistas', views.verlistas, name='verlistas'),
    path('novaLista', views.novalista, name='novalista'),
    path('novoProduto', views.novoproduto, name='novoproduto'),


    path('editar/<int:id>/', views.editar, name='editar'),
    path('update/<int:id>/', views.update, name='update')
    
]

    