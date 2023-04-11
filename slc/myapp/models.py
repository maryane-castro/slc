from django.db import models

# Create your models here.
class lista(models.Model):
    name_lista = models.CharField(max_length=100)


class produtos(models.Model):
    name_produto = models.CharField(max_length=100)