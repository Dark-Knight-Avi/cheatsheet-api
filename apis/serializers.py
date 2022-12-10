from rest_framework import serializers

from .models import Html, Css, JavaScript, Favourites

class HtmlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Html
        fields = ('title', 'description', 'code')
class CssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Css
        fields = ('title', 'description', 'code')
class JavaScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = JavaScript
        fields = ('title', 'description', 'code')
class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('title', 'description', 'code')