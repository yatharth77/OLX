from django.conf.urls import url, include
from django.urls import path
from superuser import views as superuser_views


urlpatterns = [

	path('pending', superuser_views.pending_post, name='pending'),
	url(r'^approve/(?P<id_inc>\d+)/$', superuser_views.approve, name='approve'),
	url(r'^decline/(?P<id_inc>\d+)/$', superuser_views.decline, name='decline'),
	url(r'^all_users', superuser_views.users, name='all_users'),
	]
