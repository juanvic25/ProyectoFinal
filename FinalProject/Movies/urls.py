from django.urls import path
from Movies.views import createCategory, listMovies, createMovies

urlpatterns = [
    path("createCategory/",createCategory),
    path("listMovies/",listMovies),
    path("createMovies/",createMovies),
]
