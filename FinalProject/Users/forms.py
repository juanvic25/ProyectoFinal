from django import forms
from Users.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','email','date_birth','avatar']
