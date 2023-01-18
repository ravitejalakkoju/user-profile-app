from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.models import User
from .services.subscription_service import SubscriptionService
from django.http import HttpResponseNotFound

def subscribe(request, subscription_id):
	if request.user.is_authenticated:
		if request.method == 'POST' and SubscriptionService.subscribe(subscription_id):
			return redirect('myprofile:index')
	else:
		return HttpResponseNotFound()
	return render(request, 'subscriptions/subscribe.html', {'subscription_id': subscription_id})

def unsubscribe(request, subscription_id):
	if request.user.is_authenticated:
		if request.method == 'POST' and SubscriptionService.unsubscribe(subscription_id):
			return redirect('myprofile:index')
	else:
		return HttpResponseNotFound()
	return render(request, 'subscriptions/unsubscribe.html', {'subscription_id': subscription_id})