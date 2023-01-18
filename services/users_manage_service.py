from authentication.models import User

class UsersManageService:
    def get_user(user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except:
            return False

    def delete_user(user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return True
        except:
            return False
