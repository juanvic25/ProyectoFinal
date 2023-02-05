from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    first_name  = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombres")
    last_name   = models.CharField(max_length=50, null=True, blank=True, verbose_name="Apellidos")
    email       = models.EmailField(null=True, blank=True, verbose_name="Correo Electronico")
    date_birth  = models.DateField(null=True, blank=True, verbose_name="Fecha Nacimiento")
    avatar      = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username