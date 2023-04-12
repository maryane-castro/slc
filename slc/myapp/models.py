from django.db import models
from django.forms import ModelForm


# Create your models here.
class Lista(models.Model):
    id = models.IntegerField(primary_key=True)
    name_lista = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.name_lista


class Produtos(models.Model):
    id = models.IntegerField(primary_key=True)
    name_produto = models.CharField(default= None, max_length=100)
    valor_produto = models.FloatField(default= 0)
    categoria = models.ForeignKey(Lista, on_delete=models.CASCADE, default=None)

    
    def __sizeof__(self):
        return self.id



class CriacaoListas(ModelForm):
    class Meta:
        model = Lista
        fields = ['name_lista', 'id']

class CriacaoProduto(ModelForm):
    class Meta:
        model = Produtos
        fields = ['name_produto', 'valor_produto', 'categoria', 'id']