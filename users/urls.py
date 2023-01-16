from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views

app_name = 'users'

urlpatterns = [
	path('', views.get_user_profile, name='getuserprofile'),
	path('update', views.update_user_profile, name='updateuserprofile'),
	path('delete', views.delete_user_profile, name='deleteuserprofile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)