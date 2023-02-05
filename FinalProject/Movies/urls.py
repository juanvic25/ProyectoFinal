from django.urls import path
from Movies.views import createCategory, listMovies, createMovies, updateMovie, listMoviesCategory, updateCategory

urlpatterns = [
    path("createCategory/",createCategory),
    path("updateCategory/<int:id>/",updateCategory),
    path("listMovies/",listMovies),
    path("listMoviesCategory/<int:id>/",listMoviesCategory),
    path("createMovie/",createMovies),
    path("updateMovie/<int:id>/",updateMovie),
]
