from django.contrib import admin
from Movies.models import categories

@admin.register(categories)
class categories(admin.ModelAdmin): 
    list_display = ('name','active')
