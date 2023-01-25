from django.urls import path
from django.contrib.auth.views import LogoutView
from Users.views import login_view, update_profile

urlpatterns = [
    path("login/",login_view),
    path("logout/",LogoutView.as_view(template_name='Users/logout.html')),
    path("update_profile/",update_profile),
]
