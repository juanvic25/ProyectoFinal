from django.urls import path
from Reviews.views import createReview, listReviews

urlpatterns = [
    path("createReview/",createReview),
    path("listReviews/<int:id>/",listReviews),
]