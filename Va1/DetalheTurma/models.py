from django.db import models

class DetalheTurma (models.Model):
    Aluno = models.CharField(max_length=100)
    Professor = models.CharField(max_length=100)
    Turma = models.CharField(max_length=100)