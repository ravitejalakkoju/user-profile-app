from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .services.auth_service import AuthService
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from allauth.socialaccount.forms import SignupForm

def index(request):
    return render(request, 'registration/home.html')

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if AuthService.log_in(request, request.POST):
            return redirect('myprofile:index')
        else:
            return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html', {'form':  AuthenticationForm()})

def oauth_log_in(request):
    return redirect('myprofile:index')

def oauth_sign_up(request):
    form = SignupForm()
    return render(request, 'socialaccount/ssignup.html', {'form': form})

def log_out(request):
    if AuthService.log_out(request):
        return render(request, 'registration/logout.html')
    else: 
        HttpResponse('Failed to log out')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if AuthService.register(request, request.POST):
                return redirect('authentication:index')
        return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html', {'form': RegistrationForm()})