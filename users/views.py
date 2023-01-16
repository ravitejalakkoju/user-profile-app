from django.shortcuts import render
from django.http import HttpResponse

def get_user_profile(request, user_id):
	return render(request, 'users/user-profile.html')

def edit_user_profile(request, user_id):
	return render(request, 'users/user-profile.html')

def update_user_profile(request, user_id):
	return render(request, 'users/user-profile.html')

def delete_user_profile(request, user_id):
	return render(request, 'users/user-profile.html')
