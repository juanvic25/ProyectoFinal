from django import forms
from Movies.models import category, movie

class CategoryForm(forms.ModelForm ):
    class Meta:
        model = category
        fields = '__all__'
        widgets = {
            'name': forms.Textarea(attrs={"rows":1,"cols":70}),
        }

class MovieForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=category.objects.filter(active=True))
    
    class Meta:
        model = movie
        fields = ('title','summary','director','duration','release_date','category','poster','active')
        labels = {
            'title': 'Título',
            'summary': 'Resumen',
            'director': 'Director',
            'duration': 'Duración (min)',
            'release_date': 'Estreno',
            'category': 'Categoría',
            'poster': 'Poster',
            'active': 'Activo',
        }
        widgets = {
            'title': forms.Textarea(attrs={"rows":1,"cols":100}),
            'summary': forms.Textarea(attrs={"rows":8,"cols":100}),
            'release_date':forms.DateInput(attrs={'type': 'date'}),
        }