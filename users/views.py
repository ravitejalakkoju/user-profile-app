from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UpdateUserForm	
from authentication.models import User

def get_user_profile(request, user_id):
	user = User.objects.get(id=user_id)
	return render(request, 'users/user-profile.html', {'user': user})

def update_user_profile(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		form = UpdateUserForm(request.POST, request.FILES, instance=user)
		print(len(request.FILES))
		if form.is_valid():
			form.save()
			return redirect('users:getuserprofile', user_id)
	else:
		form = UpdateUserForm(instance=user)
	return render(request, 'users/edit-user-profile.html', {'form': form})

def delete_user_profile(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		user.delete()
		return redirect('authentication:register')
	return render(request, 'users/delete-user-profile.html')

def subscription(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		user.is_subscribed = not user.is_subscribed
		user.save()
		return redirect('users:getuserprofile', user_id)
	return render(request, 'users/subscription.html')
