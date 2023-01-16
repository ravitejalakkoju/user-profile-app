from django.shortcuts import render, redirect
from authentication.models import User

def subscribe(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		user.is_subscribed = True
		user.save()
		return redirect('users:getuserprofile', user_id)
	return render(request, 'subscriptions/subscribe.html')

def unsubscribe(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		user.is_subscribed = False
		user.save()
		return redirect('users:getuserprofile', user_id)
	return render(request, 'subscriptions/unsubscribe.html')