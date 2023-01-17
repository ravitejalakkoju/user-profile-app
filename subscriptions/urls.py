from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

app_name = 'subscriptions'

urlpatterns = [
	path('<subscription_id>/subscribe', views.subscribe, name='subscribe'),
	path('<subscription_id>/unsubscribe', views.unsubscribe, name='unsubscribe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)