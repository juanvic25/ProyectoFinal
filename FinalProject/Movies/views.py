from django.shortcuts import render
from django.views.generic import ListView
from Movies.forms import CategoryForm, MovieForm
from Movies.models import category, movie
from datetime import datetime

def createCategory(request):
    categories_active = category.objects.filter(active = True)
    if request.method == 'GET':
        categories_all = category.objects.all()
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

            categories_all = category.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm()
            }
            return render(request,'Movies/categories.html',context=context)
        else:
            categories_all = category.objects.all()
            context = {
                        'categories':categories_active,
                        'categories_all':categories_all,
                        'form':CategoryForm(),
                        'errors': form.errors
            }
            return render(request,'Movies/categories.html',context=context)

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
            movie_new = movie.objects.create(
                title     = form.cleaned_data['Titulo'] ,
                summary   = form.cleaned_data['Resumen'],
                release_date = form.cleaned_data['Fecha_Estreno'],
                director  = form.cleaned_data['Director'],
                poster    = form.cleaned_data['Poster'],
                duration  = form.cleaned_data['Duracion'],
                active    = form.cleaned_data['Activo']
            )
            movie_new.category.set(form.cleaned_data['Categorias'])
            movie_new.save()
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

def updateMovie(request, id):
    categories_active = category.objects.filter(active = True)
    movie_review = movie.objects.get(id=id)
    
    if request.method == 'GET':
        form = MovieForm(initial={
                                'Titulo':movie_review.title,
                                'Resumen':movie_review.summary,
                                'Fecha_Estreno':movie_review.release_date,
                                'Director':movie_review.director,
                                'Poster':movie_review.poster,
                                'Duracion':movie_review.duration,
                                #'Categorias':movie_review.category.objects.all(),
                                'Activo':movie_review.active
                                })
        #form.changed_data['Categorias'].set(movie_review.category)
        context = {
            'categories':categories_active,
            'movie': movie_review,
            'form': form
        }
        
        return render(request,'Movies/update_movie2.html',context=context)

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie_review.title     = form.cleaned_data['Titulo'] 
            movie_review.summary   = form.cleaned_data['Resumen']
            movie_review.release_date = form.cleaned_data['Fecha_Estreno']
            movie_review.director  = form.cleaned_data['Director']
            movie_review.poster    = form.cleaned_data['Poster']
            movie_review.duration  = form.cleaned_data['Duracion']
            #movie_review.category  = form.cleaned_data['Categorias']
            movie_review.active    = form.cleaned_data['Activo']
            movie_review.save()

            context = {
                        'categories':categories_active,
                        'movies' : movie.objects.all()
                    }
            return render(request,'Movies/list_movies.html',context=context)
        else:
            context = {
                'categories':categories_active,
                'form_errores': form.errors,
                'form' : MovieForm()
            }
        return render(request,'Movies/update_movie2.html',context=context)