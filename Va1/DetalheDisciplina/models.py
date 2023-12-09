from django.db import models

class DetalheDisciplina(models.Model):
    Curso = models.CharField(max_length=100)
    Disciplina = models.CharField(max_length=100)