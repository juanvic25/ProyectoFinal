from django.contrib import admin
from Movies.models import categories, movies

@admin.register(categories)
class categories(admin.ModelAdmin): 
    list_display = ('name','active')

@admin.register(movies)
class movies(admin.ModelAdmin): 
    list_display = ('title','release_date','active')