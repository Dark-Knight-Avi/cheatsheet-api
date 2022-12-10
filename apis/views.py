from django.shortcuts import render
from .serializers import HtmlSerializer, CssSerializer, JavaScriptSerializer, FavouritesSerializer
from .models import Html, Css, Favourites, JavaScript
from rest_framework import viewsets

# Create your views here.

class HtmlViewSet(viewsets.ModelViewSet):
    queryset = Html.objects.all()
    serializer_class = HtmlSerializer
    
class CssViewSet(viewsets.ModelViewSet):
    queryset = Css.objects.all()
    serializer_class = CssSerializer
    
class JavaScriptViewSet(viewsets.ModelViewSet):
    queryset = JavaScript.objects.all()
    serializer_class = JavaScriptSerializer

class FavouritesViewSet(viewsets.ModelViewSet):
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer
