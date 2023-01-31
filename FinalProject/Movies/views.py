from django.shortcuts import render
from django.views.generic import ListView
from Movies.forms import CategoryForm, MovieForm
from Movies.models import categories, movies

def createCategory(request):
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

def createMovies(request):
    categories_active = categories.objects.filter(active = True)
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'form':MovieForm()
        }
        return render(request,'Movies/create_movies.html',context=context)
    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                        'categories':categories_active,
                        'form':MovieForm()
            }
            return render(request,'Movies/create_movies.html',context=context)
        else:
            context = {
                        'categories':categories_active,
                        'form':MovieForm(),
                        'errors': form.errors
            }
            return render(request,'Movies/create_movies.html',context=context)

def listMovies(request):
    categories_active = categories.objects.filter(active = True)
    movies_list = movies.objects.all()
    context = {
                'categories':categories_active,
                'movies' : movies_list
            }
    return render(request,'Movies/list_movies.html',context=context)


def updateMovie(request, id):
    categories_active = categories.objects.filter(active = True)
    movie = movies.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'categories':categories_active,
            'form': MovieForm(
                        initial= {
                            'title' : movie.title, 
                            'summary'   : movie.summary,
                            'release_date'   : movie.release_date,
                            'director' : movie.director,
                            'poster': movie.poster,
                            'duration'   : movie.duration,
                          #  'category'   : movie.category,
                            'active'   : movie.active,
                        }
                    )
        }
        return render(request,'Movies/update_movie.html',context=context)

    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie.title=form.cleaned_data['title'] 
            movie.summary=form.cleaned_data['summary']
            movie.release_date = form.cleaned_data['release_date']
            movie.director=form.cleaned_data['director']
            movie.poster=form.cleaned_data['poster']
            movie.duration=form.cleaned_data['duration']
         #   movie.category=form.cleaned_data['category']
            movie.active=form.cleaned_data['active']
            movie.save()
            context = {
                'categories':categories_active,
                'mensaje': 'Se Edito el Profesor correctamente'
            }
        else:
            context = {
                'categories':categories_active,
                'form_errores': form.errors,
                'form' : MovieForm()
            }
        return render(request,'Movies/update_movie.html',context=context)