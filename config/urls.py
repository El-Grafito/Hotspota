from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from scoop.views import home, cat, info, all, product_page, categorya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cat/', cat, name='cat'),
    path('info/', info, name='info'),
    path('all/', all, name='all'),
    path('categorya/<category_slug>/<pk>/', product_page, name='product_page'),
    path('categorya/<slug>/', categorya, name='categorya'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    