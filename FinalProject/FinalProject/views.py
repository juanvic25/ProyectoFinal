from django.shortcuts import render
from Movies.models import category

def index(request):
    categories_all = category.objects.filter(active = True)
    context = {'categories': categories_all}
    return render(request, 'index.html',context=context)