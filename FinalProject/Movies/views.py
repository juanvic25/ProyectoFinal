from django.shortcuts import render
from Movies.forms import CategoryForm, MovieForm
from Movies.models import category, movie

def createCategory(request):
    categories_active = category.objects.filter(active = True)
    categories_all = category.objects.all()
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'categories_all':categories_all,
                    'form':CategoryForm()
        }
        return render(request,'Movies/create_category.html',context=context)
    elif request.method == 'POST':
        form = CategoryForm(data = request.POST)
        if form.is_valid():
            category.objects.create(name=form.cleaned_data['name'], active=form.cleaned_data['active'])
            categories_all = category.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm()
            }
            return render(request,'Movies/create_category.html',context=context)
        else:
            categories_all = category.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm(),
                        'errors': form.errors
            }
            return render(request,'Movies/create_category.html',context=context)

def updateCategory(request,id):
    categories_active = category.objects.filter(active = True)
    category_select = category.objects.get(id=id)
    categories_all = category.objects.all()
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'categories_all':categories_all,
                    'form':CategoryForm(instance=category_select)
        }
        return render(request,'Movies/update_category.html',context=context)

    elif request.method == 'POST':
        form = CategoryForm(data = request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            categories_all = category.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm()
            }
            return render(request,'Movies/create_category.html',context=context)
        else:
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'errors' : form.errors,
                        'form':form
            }
            return render(request,'Movies/update_category.html',context=context)

def createMovies(request):
    categories_active = category.objects.filter(active = True)
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'form':MovieForm()
        }
        return render(request,'Movies/create_movies.html',context=context)
    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie.objects.create(
                title     = form.cleaned_data['title'] ,
                summary   = form.cleaned_data['summary'],
                release_date = form.cleaned_data['release_date'],
                director  = form.cleaned_data['director'],
                poster    = form.cleaned_data['poster'],
                duration  = form.cleaned_data['duration'],
                category  = form.cleaned_data['category'],
                active    = form.cleaned_data['active']
            )
            context = {
                        'categories':categories_active,
                        'message':'Pelicula registrada Correctamente',
                        'form':MovieForm()
            }
            return render(request,'Movies/create_movies.html',context=context)
        else:
            context = {
                        'categories':categories_active,
                        'form':MovieForm(),
                        'form_errors': form.errors
            }
            return render(request,'Movies/create_movies.html',context=context)

def updateMovie(request, id):
    categories_active = category.objects.filter(active = True)
    movie_review = movie.objects.get(id=id)
    
    if request.method == 'GET':
        context = {
            'categories':categories_active,
            'movie': movie_review,
            'form': MovieForm(instance=movie_review)
        }
        return render(request,'Movies/update_movie.html',context=context)

    elif request.method == 'POST':
        form = MovieForm(data = request.POST, files = request.FILES, instance=movie_review)
        if form.is_valid():
            form.save()
            context = {
                        'categories':categories_active,
                        'movies' : movie.objects.all()
                    }
            return render(request,'Movies/list_movies.html',context=context)
        else:
            context = {
                'categories':categories_active,
                'form_errors': form.errors,
                'form' : MovieForm(instance=movie_review)
            }
        return render(request,'Movies/update_movie.html',context=context)

def listMovies(request):
    categories_active = category.objects.filter(active = True)
    if 'search' in request.GET:
        filtro = request.GET['search']
        if request.user.is_superuser:
            movies_list = movie.objects.filter(title__contains=filtro)
        else:
            movies_list = movie.objects.filter(title__contains=filtro, active=True)
    else:
        if request.user.is_superuser:
            movies_list = movie.objects.all()
        else:
            movies_list = movie.objects.filter(active=True)
    context = {
                'categories':categories_active,
                'movies' : movies_list
            }
    return render(request,'Movies/list_movies.html',context=context)

def listMoviesCategory(request,id):
    category_select = category.objects.get(id=id)
    categories_active = category.objects.filter(active = True)
    if 'search' in request.GET:
        filtro = request.GET['search']
        if request.user.is_superuser:
            movies_list = movie.objects.filter(title__contains=filtro)
        else:
            movies_list = movie.objects.filter(title__contains=filtro, active=True)
    else:
        if request.user.is_superuser:
            movies_list = movie.objects.all()
        else:
            movies_list = movie.objects.filter(active=True)
    context = {
                'categories':categories_active,
                'category_select':category_select,
                'movies' : movies_list
            }
    return render(request,'Movies/list_movies_category.html',context=context)

