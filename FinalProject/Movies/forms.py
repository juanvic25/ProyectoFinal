from django import forms
from Movies.models import categories, movies

class CategoryForm(forms.ModelForm ):
    class Meta:
        model = categories
        fields = ['name','active']

class MovieForm(forms.ModelForm ):
    class Meta:
        model = movies
        fields = '__all__'