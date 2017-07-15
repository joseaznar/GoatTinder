from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


# Create your views here.
# here comes all de logic 
def home (request):
    if request.user.is_authenticated():
        genero = User.objects.get(email=request.user.email).genero
        usuarios = User.objects.filter(~Q(email=request.user.email,genero=genero))
        return render (request,'home.html', {'users':usuarios})
    else:
        return redirect('home:login')

def SignUp(request):

    form = SignupForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            return redirect('home:index')
    else:
        return render(request, 'signup.html', {'form': form})

def LogIn(request):

    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                return HttpResponse("El usuario no existe en la BD!")
    else:
        return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('home:login')

