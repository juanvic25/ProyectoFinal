from django import forms
from Reviews.models import review

class reviewForm(forms.ModelForm ):
    class Meta:
        model = review
        fields = ['summary','score']