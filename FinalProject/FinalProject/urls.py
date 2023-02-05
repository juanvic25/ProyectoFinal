from django.contrib import admin
from django.urls import path, include
from FinalProject.views import aboutUs
from django.conf import settings
from django.conf.urls.static import static
from Movies.views import listMovies

urlpatterns = [
    path("admin/", admin.site.urls),
    path("aboutUs/",aboutUs),
    path("", listMovies),
    path("Users/",include('Users.urls')),
    path("Movies/",include('Movies.urls')),
    path("Reviews/",include('Reviews.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
