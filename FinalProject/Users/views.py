from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from Users.forms import UserProfileForm
from Users.models import UserProfile
from Movies.models import category, movie

def login_view(request):
    categories_all = category.objects.filter(active = True)
    if request.method=='GET':
        context = {'categories': categories_all,
                    'form':AuthenticationForm}
        return render(request,'Users/login.html',context=context)

    elif request.method =='POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password=password)

            if user is not None:
                login(request,user)
                if request.user.is_superuser:
                    movies_list = movie.objects.all()
                else:
                    movies_list = movie.objects.filter(active=True)
                context={'categories': categories_all,
                            'movies':movies_list}

                return render(request,'Movies/list_movies.html',context=context)
            else:
                context = { 'categories': categories_all,
                            'error':'Contraseña Incorrecta',
                            'form':AuthenticationForm}
                return render(request,'Users/login.html',context=context)
        else:
            context = { 'categories': categories_all,
                        'error':'Contraseña Incorrecta',
                         'form':AuthenticationForm}
            return render(request,'Users/login.html',context=context)

def update_profile(request):
    categories_all = category.objects.filter(active = True)
    if request.method =='GET':
        context = {
            'categories': categories_all,
            'form': UserProfileForm(instance=request.user.profile)
        }
        return render(request,'Users/update_profile.html',context=context)
    elif request.method =='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:
                movies_list = movie.objects.all()
            else:
                movies_list = movie.objects.filter(active=True)
            context={'categories': categories_all,
                     'movies':movies_list}

            return render(request,'Movies/list_movies.html',context=context)
        else:
            context={'categories': categories_all,
                     'form_errors': form.errors,
                     'form' : UserProfileForm
                    }
            return render(request,'Users/update_profile.html',context=context)

def register(request):
    categories_all = category.objects.filter(active = True)
    if request.method=='GET':
        context = {'categories': categories_all,
                    'form':UserCreationForm}
        return render(request,'Users/register.html',context=context)
    elif request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user = user)
            return redirect('/Users/login/')
        else:
            context={
                'categories': categories_all,
                'errors': form.errors,
                'form': UserCreationForm
            }
            return render(request, 'Users/register.html',context=context)

def changePassword(request):
    categories_all = category.objects.filter(active = True)
    user = request.user
    if request.method=='GET':
        context = {'categories': categories_all,
                    'form':PasswordChangeForm(user) }
        return render(request,'Users/password.html',context=context)
    elif request.method =='POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Users/logout/')
        else:
            context={
                'categories': categories_all,
                'form': PasswordChangeForm(user),
                'errors': form.errors
            }
            return render(request, 'Users/password.html',context=context)
