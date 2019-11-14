from django.shortcuts import render
from django_apptitoso.models import *
from django_apptitoso import views
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import View, TemplateView
from django.contrib.postgres import *
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login

# Create your views here.

class RecipeListView(View):

    def get(self, request):
        # arr_features = sorted(arr_features, key=lambda x: x["name"])
        arrRecipes = []
        for r in Recipe.objects.all():
            try:
                arrRecipes.append({"key": r.pk, "name": r.name, "picture": r.picture.url, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
            except:
                arrRecipes.append({"key": r.pk, "name": r.name, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
        return JsonResponse({"arrReceitas": arrRecipes})

class FilteredRecipeListView(View):

    def get(self, request, recipeName=None, authorPk=None, tag1=None, tag2=None, tag3=None):
        resultQuery = Recipe.objects.all()
        arrRecipes = []
        if recipeName is not None:
            resultQuery = resultQuery.filter(name__icontains=recipeName)
        if authorPk is not None:
            resultQuery = resultQuery.filter(user_profile=authorPk)
        if tag1 is not None:
            resultQuery = resultQuery.filter(categories=tag1)
            if tag2 is not None:
                resultQuery = resultQuery.filter(categories=tag2)
                if tag3 is not None:
                    resultQuery = resultQuery.filter(categories=tag3)
        for r in resultQuery:
            try:
                arrRecipes.append({"key": r.pk, "name": r.name, "picture": r.picture.url, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
            except:
                arrRecipes.append({"key": r.pk, "name": r.name, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
        return JsonResponse({"arrReceitas": arrRecipes})

class FullRecipeListView(View):

    def get(self, request, key):
        # arr_features = sorted(arr_features, key=lambda x: x["name"])
        arrRecipes = []
        r = Recipe.objects.get(pk = key)
        arrIngredients = []
        for i in RecipeIngredient.objects.filter(recipe=r):
            arrIngredients.append({"ingredient": str(i.quantity)+" "+i.unit_of_measurement.name+" de "+i.ingredient.description})
        arrSteps = []
        for s in Step.objects.filter(recipe=r).order_by('step_order'):
            if s.timer is None:
                try:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "picture": s.picture.url})
                except:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description})
            else:
                try:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "picture": s.picture.url, "timer": s.timer.time})
                except:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "timer": s.timer.time})
        try:
            arrRecipes.append({"key": r.pk, "name": r.name, "description": r.description, "picture": r.picture.url, "recipeAuthorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username, "ingredients": arrIngredients, "steps": arrSteps})
        except:
            arrRecipes.append({"key": r.pk, "name": r.name, "description": r.description, "recipeAuthorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username, "ingredients": arrIngredients, "steps": arrSteps})
        return JsonResponse({"arrReceitas": arrRecipes})

class CreatedRecipeListView(View):
    def get(self, request, authorPk):
        arrRecipes = []
        for r in Recipe.objects.filter(user_profile=authorPk):
            try:
                arrRecipes.append({"key": r.pk, "name": r.name, "picture": r.picture.url, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
            except:
                arrRecipes.append({"key": r.pk, "name": r.name, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
        return JsonResponse({"arrReceitas": arrRecipes})


class SavedRecipeListView(View):
    def get(self, request, key):
        arrRecipes = []
        loggedUser = key
        u = User.objects.get(pk=loggedUser)
        for r in u.saved_recipes.all():
            try:
                arrRecipes.append({"key": r.pk, "name": r.name, "picture": r.picture.url, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
            except:
                arrRecipes.append({"key": r.pk, "name": r.name, "authorKey": r.user_profile.user.pk, "recipeAuthorName": r.user_profile.user.username})
        return JsonResponse({"arrReceitas": arrRecipes})


class PerfilView(View):

    def get(self, request, key):

        perfil = []
        loggedUser = key
        u = User.objects.get(pk=loggedUser)
        try:
            perfil.append({ "key":u.pk, "name": u.user.username, "firstName":u.user.first_name, "lastName":u.user.last_name, "picture": u.picture.url, "email": u.user.email} )
        except:
            perfil.append({ "key":u.pk, "name": u.user.username, "firstName":u.user.first_name, "lastName":u.user.last_name, "email": u.user.email} )

        return JsonResponse({"perfil": perfil})

class ChangePasswordView( View):
    def get(self, request, user, password):

        perfil = []
        u = User.objects.get(user=user)
        u.user.set_password(password)
        u.user.save()

        perfil.append({"name": u.user.username,"firstName": u.user.first_name,"lastName": u.user.last_name, "email": u.user.email} )

        return JsonResponse({"perfil": perfil})

class EditProfileInfoView(View):
    def get(self, request, key, username=None, firstname=None, lastname=None):

        u = User.objects.get(pk= key)
        if username is not None:
            u.user.username=username
        if firstname is not None:
            u.user.first_name=firstname
        if lastname is not None:
            u.user.last_name=lastname

        u.user.save()

        profile = []
        profile.append({"name": u.user.username,"firstName":u.user.first_name,"lastName":u.user.last_name ,"email": u.user.email} )

        return JsonResponse({"profile": profile})

class CulinaryConceptListView(View):
    def get(self, request):
        arrCulinaryConcept = []
        for c in CulinaryConcept.objects.all():
            arrCulinaryConcept.append({"name": c.name})
        return JsonResponse({"arrCulinaryConcept": arrCulinaryConcept})

class FullCulinaryConceptView(View):
    def get(self, request, key):
        culinaryConcept = []
        for c in CulinaryConcept.objects.filter(pk = key):
            try:
                culinaryConcept.append({"pk": c.pk, "name": c.name, "picture":c.picture, "description":c.description })
            except:
                culinaryConcept.append({"pk": c.pk, "name": c.name, "description":c.description })
        return JsonResponse({"arrCulinaryConcept": culinaryConcept})


class IndividualStepView(View):
    def get(self, request, key, recipePk):
        individualStep = []
        for s in Step.objects.filter(pk = key, recipe = recipePk):
            if s.timer is None:
                try:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "picture": s.picture})
                except:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description})
            else:
                try:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "picture": s.picture.url, "timer": s.timer.time})
                except:
                    arrSteps.append({"key": s.pk, "stepOrder": s.step_order, "description": s.description, "timer": s.timer.time})

        return JsonResponse({"individualStep": individualStep})

class SignUpView(View):
    def get(self, request, username, email, lastName, firstName, password):

        if AuthUser.objects.filter(username=username).exists():
           return JsonResponse({"signUp": "false", "problem":"Usuário já existe"})
        else:
            u = AuthUser.objects.create_user(username, email, password)
            u.last_name = lastName
            u.first_name = firstName
            u.save()
            newUser = AuthUser.objects.get(username=username)
            perfil = []
            perfil.append({ "name": newUser.username,"firstName":newUser.first_name,"lastName":newUser.last_name ,"email": newUser.email} )

            #auto login test
            logUsername = username
            logPassword = password
            user = authenticate(username=logUsername, password=logPassword)
            login(request, user)

            return JsonResponse({"signUp": perfil})

class LoginView(View):

    def get(self, request, username, password):

        if AuthUser.objects.filter(username=username).exists():
            logUsername = username
            logPassword = password
            user = authenticate(username=logUsername, password=logPassword)
            if user is not None:
                login(request, user)
                return JsonResponse({"login": "true"})
            else:
               return JsonResponse({"login": "false", "problem":"Senha incorreta"})


        else:
            return JsonResponse({"login": "false", "problem":"Usuario incorreto"})
