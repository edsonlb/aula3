from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True)
    idade = models.IntegerField()
