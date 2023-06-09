from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lista, Produtos, CriacaoListas, CriacaoProduto

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login




def naologado():
    return HttpResponse('Você nao esta logado')

def index(request):
    return render(request, 'index.html')



def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Nome de usuário já existente!")

        user = User.objects.create_user(username=username, password=senha)
        user.save()

        return HttpResponseRedirect("../../")



def login(request):
    if request.method == "GET":
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect("../verlistas")
        else:
            return HttpResponse("Email ou senha inválidos, volte e tente logar novamente.")



def verlistas(request):
    if request.user.is_authenticated:
        total = 0
        for prod in Produtos.objects.all():
            total = total + prod.valor_produto
        return render(request, 'verlistas.html', {
            "listas": Lista.objects.all(), "produtos": Produtos.objects.all, "valor" : total
        })
    naologado()


def novalista(request):
    if request.user.is_authenticated:
        formLista = CriacaoListas(request.POST or None)

        if formLista.is_valid():
            formLista.save()
            

        
        return render(request, 'criacaolista.html', {'formLista': formLista})
    
    naologado()


def novoproduto(request):
    if request.user.is_authenticated:
        formProduto = CriacaoProduto(request.POST or None)
        
        if formProduto.is_valid():
            formProduto.save()

        return render(request, 'criacaoproduto.html', {'formProduto' : formProduto})
    naologado()



def editar(request, id):
    produto = Produtos.objects.get(id=id)
    if request.user.is_authenticated:
        formProduto = CriacaoProduto(request.POST or None, instance=produto)
        
        if formProduto.is_valid():
            formProduto.save()
            return HttpResponseRedirect("../../verlistas")

        return render(request, 'update.html', {"produtos":produto, 'formProduto' : formProduto})

    

def deleteLista(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return HttpResponseRedirect("../../verlistas")

    

def deleteProduto(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    return HttpResponseRedirect("../../verlistas")