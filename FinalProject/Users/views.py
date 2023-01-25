from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from Users.forms import UserProfileForm

# Create your views here.

def login_view(request):
    if request.method=='GET':
        context = {'form':AuthenticationForm}
        return render(request,'Users/login.html',context=context)
    elif request.method =='POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password=password)

            if user is not None:
                login(request,user)
                context={'mensaje':'logueado'}
                return render(request,'index.html',context=context)
            else:
                context = { 'error':'Contraseña Incorrecta',
                            'form':AuthenticationForm}
                return render(request,'Users/login.html',context=context)
        else:
            context = { 'error':'Contraseña Incorrecta',
                                'form':AuthenticationForm}
            return render(request,'Users/login.html',context=context)

def update_profile(request):
    user = request.user
    if request.method =='GET':
        context = {
            'form' : UserProfileForm(
                        initial={
                            'first_name': user.profile.first_name,
                            'last_name' : user.profile.last_name,
                            'email'     : user.profile.email,
                            'date_birth': user.profile.date_birth,
                            'avatar'    : user.profile.avatar
                        }
                    )
        }
        return render(request,'Users/update_profile.html',context=context)
    elif request.method =='POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.first_name = form.cleaned_data['first_name']
            user.profile.last_name  = form.cleaned_data['last_name']
            user.profile.email      = form.cleaned_data['email']
            user.profile.date_birth = form.cleaned_data['date_birth']
            user.profile.avatar     = form.cleaned_data['avatar']
            user.profile.save()
            context={'mensaje':'Se Guardaron los cambios'}
            return render(request,'index.html',context=context)
        else:
            context={'form_errores': form.errors,
                     'form' : UserProfileForm
                    }
            return render(request,'Users/update_profile.html',context=context)