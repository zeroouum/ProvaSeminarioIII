from django.db import models

class Turma (models.Model):
    Codigo = models.CharField(max_length=100)
    CodigoCurso = models.CharField(max_length=100)
    