from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ConceitoCulinario(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.BinaryField(null=True)

class Usuario(models.Model):
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=64)
    nome = models.CharField(max_length=100)
    foto = models.BinaryField()
    receitas_salvas = models.ManyToMany('Receita')

class Receita(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField()
    foto = models.BinaryField(null=True)
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToMany('Categoria')

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

class Passo(models.Model):
    receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=20)
    ordem_passo = models.IntegerField()
    foto = models.BinaryField(null=True)
    timer = models.OneToOneField('PassoTimer', on_delete=models.CASCADE)

class PassoTimer(models.Model):
    tempo = models.TimeField()

class Ingrediente(models.Model):
    descricao = models.CharField(max_length=50)

class UnidadeDeMedida(models.Model):
    nome = models.CharField(max_length=50)

class ReceitaIngrediente():
    receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
    unidade_de_medida = models.ForeignKey('UnidadeDeMedida', on_delete=models.CASCADE)
    quantidade = models.DecimalField(decimal_places=2, null=True)

class AvaliacaoCriterio():
    nom_criterio = models.CharField(null=True)

class Avaliacao():
    usuario = models.ForeignKey('Usuario')
    receita = models.ForeignKey('Receita')
    criterio_de_avaliacao = models.ForeignKey('AvaliacaoCriterio')
    nota = models.PositiveSmallIntegerField(null=True)