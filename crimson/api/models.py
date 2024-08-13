from django.db import models

# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    quantidade_alunos = models.IntegerField(null=False)
    status = models.BooleanField(default=False)
    criacao = models.DateTimeField(auto_now_add=True)
    inicio = models.DateTimeField(null=False)
    final = models.DateTimeField(null=False)