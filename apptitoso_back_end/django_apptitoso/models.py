from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CulinaryConcept(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField(default='')


class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True, blank=True)
    saved_recipes = models.ManyToManyField('Recipe', blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.BinaryField(null=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', blank=True)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=20)


class Step(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    step_order = models.IntegerField()
    picture = models.BinaryField(null=True)
    timer = models.OneToOneField(
        'StepTimer', on_delete=models.CASCADE, blank=True)


class StepTimer(models.Model):
    time = models.TimeField()


class Ingredient(models.Model):
    description = models.CharField(max_length=50)


class UnitOfMeasurement(models.Model):
    class Meta:
        verbose_name_plural = 'Units of Measurement'
    name = models.CharField(max_length=50)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        'RecipeIngredient', on_delete=models.CASCADE, null=True)
    unit_of_measurement = models.ForeignKey(
        'UnitOfMeasurement', on_delete=models.CASCADE)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)


class EvaluationCriteria(models.Model):
    class Meta:
        verbose_name_plural: 'Evaluation criteria'
    name = models.CharField(null=True, max_length=40)


class Evaluation(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    evaluation_criteria = models.ForeignKey(
        'EvaluationCriteria', on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(null=True)
