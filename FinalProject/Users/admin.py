from django.contrib import admin
from Users.models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin): 
    list_display = ('user','first_name','last_name','email')