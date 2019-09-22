from django.contrib import admin

from .models import *

admin.site.register(CulinaryConcept)
admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Step)
admin.site.register(StepTimer)
admin.site.register(Ingredient)
admin.site.register(UnitOfMeasurement)
admin.site.register(RecipeIngredient)
admin.site.register(EvaluationCriteria)
admin.site.register(Evaluation)
