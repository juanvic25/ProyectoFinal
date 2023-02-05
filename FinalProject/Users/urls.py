from django.urls import path
from django.contrib.auth.views import LogoutView
from Users.views import login_view, update_profile, register, changePassword
from Movies.models import category, movie

urlpatterns = [
    path("login/",login_view),
    path("logout/",LogoutView.as_view(template_name='Movies/list_movies.html', 
                                      extra_context={'categories':category.objects.filter(active=True), 
                                                     'movies':movie.objects.filter(active=True)})),
    path("update_profile/",update_profile),
    path("register/",register),
    path("changePassword/",changePassword),
]