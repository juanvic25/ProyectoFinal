from django.db import models
from Movies.models import movie
from Users.models import UserProfile

class review(models.Model):

    scores  =   (
        (1,1),(2,2),(3,3),(4,4),(5,5)
    )
    user        = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile')
    summary     = models.TextField(max_length=5000,null=False, blank=False)
    score       = models.IntegerField(choices=scores)
    title       = models.ForeignKey(movie, on_delete=models.CASCADE, related_name='movie')
    date        = models.DateField(null=True, blank=True)