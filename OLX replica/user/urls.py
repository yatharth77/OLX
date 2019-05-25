from django.conf.urls import url, include
from django.urls import path
from user import views as user_views


urlpatterns = [
	path('', user_views.register, name='register'),
]