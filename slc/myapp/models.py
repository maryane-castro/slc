from django.db import models
from django.forms import ModelForm


# Create your models here.
class Lista(models.Model):
    name_lista = models.CharField(max_length=100)


class Produtos(models.Model):
    name_produto = models.CharField(default= None, max_length=100)
    categoria = models.ForeignKey(Lista, on_delete=models.CASCADE, default=None)



class CriacaoListas(ModelForm):
    class Meta:
        model = Lista
        fields = ['name_lista']

class CriacaoProduto(ModelForm):
    class Meta:
        model = Produtos
        fields = ['name_produto', 'categoria']