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
from superuser import views as superuser_views
from django.conf.urls.static import static
from django.conf import settings
from products.models import category

urlpatterns = [

    path('register/',include('user.urls')),
    path('home/admin/', include('superuser.urls')),
    path('home/', include('products.urls')),


    
    url(r'^home/password-reset/$', 
        auth_views.PasswordResetView.as_view(template_name ='users/password_reset_form.html'), 
        name='password_reset'),
    url(r'^home/password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name ='users/password_reset_done.html'), 
        name='password_reset_done'),
    url(r'^home/password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^home/reset/done/$', 
        auth_views.PasswordResetView.as_view(template_name = 'users/password_reset_complete.html'), 
        name='password_reset_complete'),

    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html',
        redirect_authenticated_user=True), name='login'),

    path('logout/', auth_views.LogoutView.as_view(extra_context={'list':category.objects.all()},next_page="../home/")),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


