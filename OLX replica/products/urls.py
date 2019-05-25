from django.conf.urls import url, include
from django.conf import settings
from products import views as product_views
from django.urls import path

urlpatterns = [
		path('', product_views.home, name='home'),
		
		path('profile/', product_views.profile, name='profile'), 
		
		url(r'upload/$', product_views.upload, name='upload'),
		url(r'^profile/delete/(?P<status>\w+)/(?P<id_inc>\d+)', 
			product_views.delete_product, name='delete'),
		url(r'^(?P<category>\w+)/$', product_views.display, name='display'),
]