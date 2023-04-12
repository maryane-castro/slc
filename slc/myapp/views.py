from django.shortcuts import render
from django.http import HttpResponse
from .models import Lista, Produtos, CriacaoListas, CriacaoProduto
# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')



def login(request):
    return render (request, 'login.html')

def index(request):
    return render(request, 'index.html', {
        "listas": Lista.objects.all(), "produtos": Produtos.objects.all
    })

def novalista(request):
    formLista = CriacaoListas(request.POST or None)
    formProduto = CriacaoProduto(request.POST or None)

    if formLista.is_valid():
        formLista.save()
        

    if formProduto.is_valid():
        formProduto.save()
        

    return render(request, 'criacao.html', {'formLista': formLista, 'formProduto' : formProduto})