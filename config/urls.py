from django.contrib import admin
from django.urls import path
from scoop.views import home
from scoop.views import cat
from scoop.views import info
from scoop.views import all
from django.conf import settings
from django.conf.urls.static import static
from scoop.views import product_page
from scoop.views import categorya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('cat/', cat),
    path('info/', info),
    path('all/', all),
    path('all/<pk>/', product_page),
    path('categorya/<pk>/', categorya),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    