from django.shortcuts import render
from Movies.models import category

def aboutUs(request):
    categories_all = category.objects.filter(active = True)
    context = {'categories': categories_all}
    return render(request, 'about_us.html',context=context)