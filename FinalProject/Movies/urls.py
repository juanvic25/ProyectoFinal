from django.urls import path
from Movies.views import createCategory

urlpatterns = [
    path("createCategory/",createCategory),
]
