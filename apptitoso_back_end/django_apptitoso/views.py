from django.shortcuts import render

# Create your views here.
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


class RecipeListView(LoginRequiredMixin, View):
    '''
    Created on XXX de XXX de XXX

    @author: Daniel Hasan Dalip <hasan@decom.cefetmg.br>
    Lista todas as receitas
    '''


    def get(self, request,nam_language):


        arr_features = sorted(arr_features, key=lambda x: x['name'])
        return JsonResponse({"arrFeatures":arr_features})
