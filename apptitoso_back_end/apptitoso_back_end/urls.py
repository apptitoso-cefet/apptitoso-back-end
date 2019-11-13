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
from django.urls import include
from django_apptitoso import views
from django.conf.urls import url

recipeFilterUrlTagPatterns = [
    url(r'tag1:(?P<tag1>[0-9]+)/$', views.FilteredRecipeListView.as_view()),
    url(r'tag1:(?P<tag1>[0-9]+)/tag2:(?P<tag2>[0-9]+)/$', views.FilteredRecipeListView.as_view()),
    url(r'tag1:(?P<tag1>[0-9]+)/tag2:(?P<tag2>[0-9]+)/tag3:(?P<tag3>[0-9]+)/$', views.FilteredRecipeListView.as_view())
]

recipeFilterUrlPatterns = [
    url(r'recipeName:(?P<recipeName>[A-zÀ-ÿ0-9_ ]+)/', include(recipeFilterUrlTagPatterns)),
    url(r'recipeName:(?P<recipeName>[A-zÀ-ÿ0-9_ ]+)/$', views.FilteredRecipeListView.as_view()),
    url(r'authorPk:(?P<authorPk>[0-9]+)/', include(recipeFilterUrlTagPatterns)),
    url(r'authorPk:(?P<authorPk>[0-9]+)/$', views.FilteredRecipeListView.as_view()),
    url(r'', include(recipeFilterUrlTagPatterns)),
]

nameUrlPatterns = [
    url(r'firstname:(?P<firstname>[A-zÀ-ÿ ]+)/$', views.EditProfileInfoView.as_view()),
    url(r'firstname:(?P<firstname>[A-zÀ-ÿ ]+)/lastname:(?P<lastname>[A-zÀ-ÿ ]+)/$', views.EditProfileInfoView.as_view()),
    url(r'lastname:(?P<lastname>[A-zÀ-ÿ ]+)/', views.EditProfileInfoView.as_view()),
]

usernameUrlPatterns = [
    url(r'username:(?P<username>[A-zÀ-ÿ0-9_.@+-]+)/', include(nameUrlPatterns)),
    url(r'username:(?P<username>[A-zÀ-ÿ0-9_.@+-]+)/$',  views.EditProfileInfoView.as_view()),
    url(r'', include(nameUrlPatterns))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^listRecipe$", views.RecipeListView.as_view()),
    url(r'^listFilteredRecipe/', include(recipeFilterUrlPatterns)),
    url(r"^listFullRecipe/(?P<key>[\d+]+)/$", views.FullRecipeListView.as_view()),
    url(r"^listSavedRecipe/$", views.SavedRecipeListView.as_view()),
    url(r"^perfil/$", views.PerfilView.as_view()),
    url(r'^editProfile', include(usernameUrlPatterns)),
    url(r'^changePassword/(?P<user>[0-9]+)/(?P<password>[A-zÀ-ÿ0-9_.@+-]+)/$', views.ChangePasswordView.as_view()),
    url(r"^listCulinaryConcept$", views.CulinaryConceptListView.as_view()),
    url(r"^fullCulinaryConcept/(?P<key>[\w-]+)/$", views.FullCulinaryConceptView.as_view()),
    url(r"^individualStep/(?P<key>[\w-]+)/(?P<recipePk>\w+)/", views.IndividualStepView.as_view()),
    url(r"^signUp/(?P<username>[^/]+)/(?P<email>[^/]+)/(?P<firstName>[^/]+)/(?P<lastName>[^/]+)/(?P<password>[^/]+)/$", views.SignUpView.as_view()),
    # url(r'^featureSetConfigajaxNew$', views.FeatureSetInsertAJAX.as_view(), name='feature_set_insertAJAX'),#Test:OK
    # url(r'^featureSetConfigajax$', views.FeatureSetEditAJAX.as_view(), name='feature_set_editAJAX'),#Test:OK
]
