from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ConceitoCulinario(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.BinaryField(null=True)
    descricao = models.TextField(default='')
    
class Usuario(models.Model):
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=64)
    nome = models.CharField(max_length=100)
    foto = models.BinaryField()
    receitas_salvas = models.ManyToManyField('Receita')

class Receita(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    foto = models.BinaryField(null=True)
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToManyField('Categoria')

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

class ReceitaIngrediente(models.Model):
    receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
    unidade_de_medida = models.ForeignKey('UnidadeDeMedida', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class AvaliacaoCriterio(models.Model):
    nom_criterio = models.CharField(null=True, max_length=40)

class Avaliacao(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
    criterio_de_avaliacao = models.ForeignKey('AvaliacaoCriterio', on_delete=models.CASCADE)
    nota = models.PositiveSmallIntegerField(null=True)
