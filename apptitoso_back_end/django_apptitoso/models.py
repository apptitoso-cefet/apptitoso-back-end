from django.db import models

class ConceitoCulinario(models.Model):
    cod_conceito = models.AutoField(primary_key=True)
    nom_conceito = models.CharField(max_length=50)
    foto_conceito = models.BinaryField(null=True)

class Usuario(models.Model):
    cod_email = models.CharField(max_length=100, primary_key=True)
    des_senha = models.CharField(max_length=64)
    nom_usuario = models.CharField(max_length=100)
    foto_usuario = models.BinaryField()
    receitas_salvas = models.ManyToMany('Receita')

class Receita(models.Model):
    cod_receita = models.AutoField(primary_key=True)
    nom_receita = models.CharField(max_length=50)
    des_receita = models.CharField()
    foto_receita = models.BinaryField(null=True)
    des_email = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToMany('Categoria')

class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    nom_categoria = models.CharField(max_length=20)

class Passo(models.Model):
    # PFK de receita
    cod_passo = models.AutoField(primary_key=True)
    des_passo = models.CharField(max_length=20)
    ordem_passo = models.IntegerField()
    foto_passo = models.BinaryField()

class PassoTimer(models.Model):
    # Falta chave
    pass

class Ingrediente(models.Model):
    des_ingredientes = models.CharField(max_length=50)

class UnidMedida(models.Model):
    nom_unid_medida = models.CharField(max_length=50)

class ReceitaIngrediente():
    pass

class AvaliacaoCriterio():
    nom_criterio = models.CharField

class Avaliacao():
    pass