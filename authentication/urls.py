from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

app_name = 'authentication'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.log_in, name='login'),
	path('logout/', views.log_out, name='logout'),
	path('signup/', views.sign_up, name='signup'),
	path('accounts/profile/', views.oauth_log_in, name="oauthlogin")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)