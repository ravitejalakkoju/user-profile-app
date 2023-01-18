from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views

app_name = 'myprofile'

urlpatterns = [
	path('', views.my_profile, name='index'),
	path('update', views.update_my_profile, name='update'),
	path('delete', views.delete_my_profile, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)