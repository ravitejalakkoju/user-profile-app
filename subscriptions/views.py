from django.shortcuts import render, redirect
from authentication.models import User
from .services.subscription_service import SubscriptionService

def subscribe(request, subscription_id):
	if request.user.is_authenticated:
		if request.method == 'POST' and SubscriptionService.subscribe(subscription_id):
			return redirect('users:getuserprofile', request.user.id)
	else:
		return redirect('authentication:login')
	return render(request, 'subscriptions/subscribe.html', {'subscription_id': subscription_id})

def unsubscribe(request, subscription_id):
	if request.user.is_authenticated:
		if request.method == 'POST' and SubscriptionService.unsubscribe(subscription_id):
			return redirect('users:getuserprofile', request.user.id)
	else:
		return redirect('authentication:login')
	return render(request, 'subscriptions/unsubscribe.html', {'subscription_id': subscription_id})