from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    first_name  = models.CharField(max_length=50, null=True, blank=True)
    last_name   = models.CharField(max_length=50, null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)
    date_birth  = models.DateField(null=True, blank=True)
    avatar      = models.ImageField(upload_to='avatar', null=True, blank=True)
