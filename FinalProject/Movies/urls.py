from django.urls import path
from Movies.views import createCategory, listMovies, createMovies, updateMovie

urlpatterns = [
    path("createCategory/",createCategory),
    path("listMovies/",listMovies),
    path("createMovie/",createMovies),
    path("updateMovie/<int:id>/",updateMovie),
]
