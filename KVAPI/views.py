from django.shortcuts import get_list_or_404, redirect, render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from . import models, serializer, forms
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView, DetailView, View, CreateView


class KeyValueApi(ListAPIView, CreateAPIView):
    queryset = models.KeyValueModel.objects.all()
    serializer_class = serializer.KeyValueSerializer
    
class KeyValueDetailID(CreateAPIView,RetrieveAPIView):
    queryset = models.KeyValueModel
    serializer_class = serializer.KeyValueSerializer

class KeyValueDetailSlug(CreateAPIView,APIView):    
    queryset = models.KeyValueModel
    serializer_class = serializer.KeyValueSerializer
    def get(self, request, slug):
        queryset = get_list_or_404(models.KeyValueModel, key=slug)[-1]
        serializers = serializer.KeyValueSerializer(queryset)
        return Response(data=serializers.data, status=status.HTTP_200_OK)    

class KeyValueHistory(APIView):    
    def get(self, request, slug):
        queryset = get_list_or_404(models.KeyValueModel, key=slug)
        serializers = serializer.KeyValueSerializer(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    
    
    
class HomeView(TemplateView):
    template_name = "KVAPI/index.html"

class KeyView(TemplateView):
    template_name = "KVAPI/chose.html"
    def post(self, request):
        key = request.POST["key"]
        return redirect("key/"+key)

class KeyValueDetail(View):
    def get(self, request, slug):
        queryset = get_list_or_404(models.KeyValueModel, key=slug)[-1]
        return render(request, "KVAPI/chose.html", context={"key":queryset}) 

class KeyValueHistoryEn(TemplateView):
    template_name = "KVAPI/chose.html"
    def post(self, request):
        key = request.POST["key"]
        return redirect("history/"+key)

class KeyValueHistory(View):
    def get(self, request, slug):
        print(slug)
        queryset = get_list_or_404(models.KeyValueModel, key=slug)[::-1]
        print(queryset)
        return render(request, "KVAPI/chose.html", context={"keys":queryset}) 

class KeyValueSet(CreateView):
    template_name = "KVAPI/set.html"
    form_class = forms.KeyvalueForm
    model = models.KeyValueModel
    success_url = "/"
