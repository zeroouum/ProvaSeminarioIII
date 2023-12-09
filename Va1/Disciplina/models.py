from django.db import models

class Disciplina (models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)