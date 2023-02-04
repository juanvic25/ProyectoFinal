from django import forms
from Movies.models import category

class CategoryForm(forms.ModelForm ):
    class Meta:
        model = category
        fields = ['name','active']

class MovieForm(forms.Form):

    Titulo       = forms.CharField(widget=forms.Textarea(attrs={"rows":1,"cols":100}),required=True)
    Resumen      = forms.CharField(widget=forms.Textarea(attrs={"rows":8,"cols":100}),required=True)
    Director     = forms.CharField(max_length=100, required=True)
    Duracion     = forms.IntegerField(label="Duración (min)", required=False)
    Fecha_Estreno= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Estreno")
    Categorias   = forms.ModelMultipleChoiceField(queryset=category.objects.filter(active=True))
    Poster       = forms.ImageField(required=False)
    Activo       = forms.BooleanField(required=False,initial=True)