"""apptitoso_back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_apptitoso import views
from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^listRecipe$", views.RecipeListView.as_view()),
    url(r"^listFullRecipe$", views.FullRecipeListView.as_view()),
    url(r"^listSavedRecipe$", views.SavedRecipeListView.as_view()),
    url(r"^perfil$", views.PerfilView.as_view()),
    #url(r"^lalal$", views.RecipeIngredientView.as_view()),
    # url(r'^featureSetConfigajaxNew$', views.FeatureSetInsertAJAX.as_view(), name='feature_set_insertAJAX'),#Test:OK
    # url(r'^featureSetConfigajax$', views.FeatureSetEditAJAX.as_view(), name='feature_set_editAJAX'),#Test:OK
]
