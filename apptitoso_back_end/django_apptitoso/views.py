from django.shortcuts import render
from django_apptitoso.models import *
from django_apptitoso import views
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import View, TemplateView

# Create your views here.
"""
class RecipeInsertAJAX(View):

    def get(self, request):

        arrCreateFeatureSet =  json.loads(request.POST["arrCreateElementsFeatureSet"])[0]
        arrErr = []

        if arrCreateFeatureSet["nam_feature_set"] is None:
            arrErr.append("Feature Set Name is required")

        if not arrErr:
            if not arrCreateFeatureSet["language"]:
                arrErr.append("Language is required")

        if not arrErr:
            try:
                with transaction.atomic():
                    languageFeature =  Language.objects.get(id=int(arrCreateFeatureSet["language"]))
                    objFeatureSet = FeatureSet.objects.create(user=self.request.user,
                                                          nam_feature_set = arrCreateFeatureSet["nam_feature_set"],
                                                          dsc_feature_set = arrCreateFeatureSet["dsc_feature_set"],
                                                          language = languageFeature,
                                                          bol_is_public=arrCreateFeatureSet["bol_is_public"]
                                                          )
                    arrCreateFeatureSet["nam_feature_set"] = objFeatureSet.nam_feature_set;

            except IntegrityError:
                lst_featureSet = FeatureSet.objects.filter(user=self.request.user,
                                                          nam_feature_set = arrCreateFeatureSet["nam_feature_set"])

                if lst_featureSet:
                    arrErr.append("Feature Set with this name already exists.")
                else:
                    arrErr.append("Could not insert the feature set.")

        return JsonResponse({"arrCreateFeatureSet" : arrCreateFeatureSet,
                             "arrErr": arrErr })


"""


class RecipeListView(LoginRequiredMixin, View):
    """
    Created on XXX de XXX de XXX

    @author: Daniel Hasan Dalip <hasan@decom.cefetmg.br>
    Lista todas as receitas
    """

    def get(self, request):
        # arr_features = sorted(arr_features, key=lambda x: x["name"])
        arrRecipes = []
        for r in Recipe.objects.all():
            arrRecipes.append({"name": r.name, "user": request.user.pk, "recipeAuthorName": r.user_profile.user.username})
        return JsonResponse({"arrReceitas": arrRecipes})

class FullRecipeListView(View):

    def get(self, request):
        # arr_features = sorted(arr_features, key=lambda x: x["name"])
        arrRecipes = []
        for r in Recipe.objects.all():
            arrIngredients = []
            for i in RecipeIngredient.objects.filter(recipe=r):
                arrIngredients.append({"ingredient": str(i.quantity)+" "+i.unit_of_measurement.name+" de "+i.ingredient.description})
            arrSteps = []
            for s in Step.objects.filter(recipe=r):
                if s.timer is None:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description})
                else:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "timer": s.timer.time})
            arrRecipes.append({"name": r.name, "description": r.description, "picture": r.picture, "recipeAuthorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username, "ingredients": arrIngredients, "steps": arrSteps})
        return JsonResponse({"arrReceitas": arrRecipes})
