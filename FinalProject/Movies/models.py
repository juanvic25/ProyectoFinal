from django.db import models

class category(models.Model):
    name   = models.CharField(max_length=100)
    active = models.BooleanField( default=True)

    def __str__(self):
        return self.name

class movie(models.Model):
    title       = models.CharField(max_length=100,null=False, blank=False)
    summary     = models.TextField(max_length=1000,null=False, blank=False)
    release_date= models.DateField(null=True, blank=True)
    director    = models.CharField(max_length=100,null=True, blank=True)
    poster      = models.ImageField(upload_to='poster', null=True, blank=True)
    duration    = models.IntegerField(null=True, blank=True)
    category    = models.ManyToManyField(category)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    