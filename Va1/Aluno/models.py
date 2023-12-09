from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    DataNascimento= models.CharField(max_length=100)
    Matricula = models.CharField(max_length=100)