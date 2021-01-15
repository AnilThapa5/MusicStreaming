from xml.etree.ElementInclude import include

from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('index', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('search', views.search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
