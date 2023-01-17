from django.contrib.auth import authenticate, login, logout
from authentication.models import User

class AuthService:
    def log_in(request, user):
        authenticated_user = authenticate(request, username=user['username'], password=user['password'])
        if authenticated_user is not None:
            login(request, authenticated_user)
            return True
        else:
            return False

    def log_out(request):
        try:
            logout(request)
            return True
        except:
            return False

    def register(request, user):
        try:
            new_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password1'])
            new_user.save()
            
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            login(request, authenticated_user)
            
            return True
        except:
            return False