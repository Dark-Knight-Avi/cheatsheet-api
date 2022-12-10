from django.urls import path, include
from rest_framework import routers
from .views import HtmlViewSet, CssViewSet, JavaScriptViewSet, FavouritesViewSet

router = routers.DefaultRouter()
router.register(r'html', HtmlViewSet)
router.register(r'css', CssViewSet)
router.register(r'javascript', JavaScriptViewSet)
router.register(r'favourites', FavouritesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
