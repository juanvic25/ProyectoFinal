from django.shortcuts import render
from Movies.forms import CategoryForm
from Movies.models import categories

def createCategory(request):
    print(1)
    categories_active = categories.objects.filter(active = True)
    if request.method == 'GET':
        categories_all = categories.objects.all()
        context = {
                    'categories':categories_active,
                    'categories_all':categories_all,
                    'form':CategoryForm()
        }
        return render(request,'Movies/categories.html',context=context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            categories_all = categories.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm()
            }
            return render(request,'Movies/categories.html',context=context)
        else:
            categories_all = categories.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm(),
                        'errors': form.errors
            }
            return render(request,'Movies/categories.html',context=context)
