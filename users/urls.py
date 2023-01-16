from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

app_name = 'users'

urlpatterns = [
	path('<user_id>/', views.get_user_profile, name='getuserprofile'),
	path('<user_id>/update/', views.update_user_profile, name='updateuserprofile'),
	path('<user_id>/delete', views.delete_user_profile, name='deleteuserprofile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)