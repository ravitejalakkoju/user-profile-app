from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .services.auth_service import AuthService
from .forms import RegistrationForm, CustomAuthenticationForm

def index(request):
    if request.user.is_authenticated:    
        return redirect('users:getuserprofile', request.user.id)
    else:
        return redirect('authentication:login')

def log_in(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if AuthService.log_in(request, request.POST):
            return redirect('users:getuserprofile', request.user.id)
        else:
            return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html', {'form':  CustomAuthenticationForm()})

def logged_in(request):
    return render(request, 'base.html')

def log_out(request):
    if AuthService.log_out(request):
        return render(request, 'registration/logout.html')
    else: 
        HttpResponse('Failed to log out')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if AuthService.register(request, request.POST):
                return redirect('users:getuserprofile', request.user.id)
        return render(request, 'registration/register.html', {'form': form})
    return render(request, 'registration/register.html', {'form': RegistrationForm()})