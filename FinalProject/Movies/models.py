from django.db import models

class category(models.Model):
    name   = models.CharField(max_length=100, verbose_name="Nombre")
    active = models.BooleanField( default=True, verbose_name="Activo")

    def __str__(self):
        return self.name

class movie(models.Model):
    title       = models.CharField(max_length=100,null=False, blank=False)
    summary     = models.TextField(max_length=1000,null=False, blank=False)
    release_date= models.DateField(null=True, blank=True)
    director    = models.CharField(max_length=100,null=True, blank=True)
    poster      = models.ImageField(upload_to='poster', null=True, blank=True)
    duration    = models.IntegerField(null=True, blank=True)
    category    = models.ForeignKey(category, on_delete=models.CASCADE, related_name='category',null=False, blank=False)
    active      = models.BooleanField(default=True)
    score       = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title