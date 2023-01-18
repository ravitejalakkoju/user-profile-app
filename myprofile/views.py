from django.shortcuts import render, redirect
from .forms import UpdateUserForm	
from authentication.models import User
from django.http import HttpResponseNotFound
from services.users_manage_service import UsersManageService
from collections import namedtuple

def my_profile(request):
	if request.user.is_authenticated:
		user = UsersManageService.get_user(request.user.id)
		return render(request, 'myprofile/my-profile.html', {'user': user})
	return HttpResponseNotFound()

def update_my_profile(request):
	if request.user.is_authenticated:
		user = UsersManageService.get_user(request.user.id)
		if request.method == 'POST':
			form = UpdateUserForm(request.POST, request.FILES, instance=user)
			if form.is_valid():
				form.save()
				return redirect('myprofile:index')
		else:
			form = UpdateUserForm(instance=user)
		return render(request, 'myprofile/edit-my-profile.html', {'form': form})
	return HttpResponseNotFound()

def delete_my_profile(request):
	if request.method == 'POST':
		if UsersManageService.delete_user(request.user.id):
			return redirect('authentication:register')
		else:
			return render(request, 'myprofile/delete-my-profile.html')
	return render(request, 'myprofile/delete-my-profile.html')
