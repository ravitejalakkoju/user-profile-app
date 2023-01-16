from django.shortcuts import render
from django.http import HttpResponse

def userprofile(request, user_id):
	return HttpResponse('This is a user profile')
