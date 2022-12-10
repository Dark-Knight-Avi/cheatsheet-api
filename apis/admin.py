from django.contrib import admin
from .models import Html
from .models import Css
from .models import JavaScript
from .models import Favourites
# Register your models here.

admin.site.register(Html)
admin.site.register(Css)
admin.site.register(JavaScript)
admin.site.register(Favourites)
admin.site.site_header = "Yo!CheatSheet Admin"
admin.site.site_title = "Yo!CheatSheet"
admin.site.index_title = "Welcome to The best HTML CSS JS Cheatsheet Admin Panel"