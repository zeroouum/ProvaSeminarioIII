from django.db import models

class DetalheCurso (models.Model):
   Codigo = models.CharField(max_length=100)
   Turma = models.CharField(max_length=100)
