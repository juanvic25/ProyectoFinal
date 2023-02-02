from django import forms
from Movies.models import category, movie

class CategoryForm(forms.ModelForm ):
    class Meta:
        model = category
        fields = ['name','active']

class MovieForm(forms.ModelForm ):
    class Meta:
        model = movie
        fields = '__all__'