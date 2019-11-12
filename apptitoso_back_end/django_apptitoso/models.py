from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import models as authModels


class CulinaryConcept(models.Model):
    name = models.CharField(max_length=50)
    picture = models.BinaryField(null=True, blank=True)
    description = models.TextField(default='')


class User(models.Model):
    user = models.ForeignKey(authModels.User, models.PROTECT)
    picture =  models.BinaryField(null=True)

    saved_recipes = models.ManyToManyField(
        'Recipe', blank=True, related_name="user_recipe")


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.BinaryField(null=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)


class Step(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    description = models.TextField()
    step_order = models.IntegerField()
    picture = models.BinaryField(null=True)
    timer = models.OneToOneField(
        'StepTimer', on_delete=models.CASCADE, null=True, blank=True)


class StepTimer(models.Model):
    time = models.DurationField()


class Ingredient(models.Model):
    description = models.CharField(max_length=50)


class UnitOfMeasurement(models.Model):
    class Meta:
        verbose_name_plural = 'Units of Measurement'
    name = models.CharField(max_length=50)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, null=True)
    unit_of_measurement = models.ForeignKey(
        'UnitOfMeasurement', on_delete=models.CASCADE)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)


class EvaluationCriterion(models.Model):
    class Meta:
        verbose_name_plural: 'Evaluation criteria'
    name = models.CharField(null=True, max_length=40)


class Evaluation(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    evaluation_criterion = models.ForeignKey(
        'EvaluationCriterion', on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(null=True)
