from django.db import models

class ConceitoCulinario(object):
    cod_conceito = models.CharField(max_length=20, primary_key=True)
    nom_conceito = models.CharField(max_length=50)