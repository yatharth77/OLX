"""olx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from user import views as user_views
from products import views as product_views
from django.conf.urls.static import static
from django.conf import settings
from products.models import category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    # path('login/', user_views.login_success),
    path('logout/', auth_views.LogoutView.as_view(extra_context={'list':category.objects.all()},next_page="../home/")),
    path('home/profile/', product_views.profile, name='profile'), 
    url(r'^home/profile/delete/(?P<status>\w+)/(?P<id_inc>\d+)', product_views.delete_product, name='delete'),
    # url(r'^home/profile/edit/(?P<status>\w+)/(?P<id_inc>\d+)', user_views.edit_product, name='edit'),                               
    path('home/', user_views.home, name='home'),
    # path('accounts/profile/', user_views.profile, name='profile'),
    path('home/pending/', product_views.pending_post, name='pending'),
    url(r'home/upload/$', product_views.upload, name='upload'),
    url(r'^home/pending/approve/(?P<id_inc>\d+)/$', product_views.approve, name='approve'),
    url(r'^home/pending/decline/(?P<id_inc>\d+)/$', product_views.decline, name='decline'),
    url(r'^home/(?P<category>\w+)/$', product_views.display, name='display'),
    url(r'home/upload/$', product_views.upload, name='upload')

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


