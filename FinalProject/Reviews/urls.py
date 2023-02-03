from django.urls import path
from Reviews.views import createReview, listReviews, deleteReview, updateReview

urlpatterns = [
    path("createReview/<int:id>/",createReview),
    path("listReviews/<int:id>/",listReviews),
    path("deleteReview/<int:id>/<int:id_movie>/",deleteReview),
    path("updateReview/<int:id>/<int:id_movie>/",updateReview),
]