from django.contrib import admin
from Movies.models import category, movie

@admin.register(category)
class categoryAdmin(admin.ModelAdmin): 
    list_display = ('name','active')

@admin.register(movie)
class movieAdmin(admin.ModelAdmin): 
    list_display = ('title','release_date','score','active')