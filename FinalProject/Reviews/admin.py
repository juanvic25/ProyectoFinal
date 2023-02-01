from django.contrib import admin
from Reviews.models import review

@admin.register(review)
class ReviewAdmin(admin.ModelAdmin): 
    list_display = ('user','title','score')