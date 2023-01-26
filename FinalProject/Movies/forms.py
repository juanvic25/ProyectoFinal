from django import forms
from Movies.models import categories

class CategoryForm(forms.ModelForm ):
    class Meta:
        model = categories
        fields = ['name','active']