from django.shortcuts import render
from Movies.models import categories

def index(request):
    categories_all = categories.objects.filter(active = True)
    context = {'categories': categories_all}
    return render(request, 'index.html',context=context)