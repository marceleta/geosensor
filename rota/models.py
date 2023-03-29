from django.db import models
from core.models import ModelTemplate


class Rota(ModelTemplate):
    nome = models.CharField('Nome rota', max_length=100, null=False)
    descricao = models.CharField('Descrição', max_length=255, null=True)
    