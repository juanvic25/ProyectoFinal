from django.urls import path
from Movies.views import createCategory, listMovies, createMovies, updateMovie, listMoviesCategory

urlpatterns = [
    path("createCategory/",createCategory),
    path("listMovies/",listMovies),
    path("listMoviesCategory/<int:id>/",listMoviesCategory),
    path("createMovie/",createMovies),
    path("updateMovie/<int:id>/",updateMovie),
]
