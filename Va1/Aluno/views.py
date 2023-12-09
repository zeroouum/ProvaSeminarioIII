from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoView(generics.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
