from django.shortcuts import render, redirect
from .forms import UpdateUserForm	
from authentication.models import User
from django.http import HttpResponseNotFound
from .services.user_manage_service import UserManageService
from collections import namedtuple

def get_user_profile(request, user_id):
	if request.user.is_authenticated:
		user = UserManageService.get_user(user_id)
		return render(request, 'users/user-profile.html', {'user': user})
	return HttpResponseNotFound()

def update_user_profile(request, user_id):
	if request.user.is_authenticated:
		user = UserManageService.get_user(user_id)
		if request.method == 'POST':
			form = UpdateUserForm(request.POST, request.FILES, instance=user)
			if form.is_valid():
				form.save()
				return redirect('users:getuserprofile', user_id)
		else:
			form = UpdateUserForm(instance=user)
		return render(request, 'users/edit-user-profile.html', {'form': form})
	return HttpResponseNotFound()

def delete_user_profile(request, user_id):
	if request.method == 'POST':
		if UserManageService.delete_user(user_id):
			return redirect('authentication:register')
		else:
			return render(request, 'users/delete-user-profile.html')
	return render(request, 'users/delete-user-profile.html')
