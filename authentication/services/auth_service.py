from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from authentication.models import User

class AuthService:
    def log_in(request, user):
        user = authenticate(request, username=user['username'], password=user['password'])
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    def log_out(request):
        try:
            logout(request)
            return True
        except:
            return False

    def register(user):
        try:
            new_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password1'])
            new_user.save()
            return True
        except:
            return False