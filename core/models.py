from venv import create
from django.db import models

# Create your models here.

class ModelTemplate(models.Model):

    create = models.DateField('criado em', auto_now_add=True,editable=False)
    modified = models.DateField('modificado em', auto_now=True,editable=False)

    class Meta:
        abstract = True
