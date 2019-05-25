from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from products.models import category
from django.contrib.auth.views import login as contrib_login

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.contrib.auth.models import User

def register(request):
	if request.user.is_authenticated == False:
		# print("HHIII")
		if request.method=="POST":
			form =UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				# send_mail(subject,message,from_email,to_list, fail_silently=True)
				subject = "Thankyou for your registeration"
				message = "Your are now member of our family"
				from_email = settings.EMAIL_HOST_USER
				to_list = [form.cleaned_data["email"]]
				send_mail(subject,message,from_email,to_list, fail_silently=True)

				username=form.cleaned_data["username"]
				messages.success(request, f'Account created successfully')
				return redirect("/home/")
		else:
			form=UserRegisterForm()
		context = {
		"form":form,
		}
		return render(request, "users/register.html", context)
	else:
		return redirect('home')

# def edit_product(request, *args, **kwargs):
# 	if request.user.is_authenticated:
# 		status=kwargs["status"]
# 		id_inc=kwargs["id_inc"]
# 		# print(status,id_inc)
# 		if status=="pending":
# 			qs=pending.objects.all()
# 		else:
# 			qs=Product.objects.all()
# 		if request.method=="POST":
# 			form =UserRegisterForm(request.POST,initial={'user_name': request.user.username,''})
# 			if form.is_valid():
# 				form.save()
# 				username=form.cleaned_data["username"]
# 				messages.success(request, f'Account created successfully')
# 				return redirect("/home/")
# 		else:
# 			form=UserRegisterForm()
# 		context = {
# 		"form":form,
# 		}
# 		return render(request, "users/register.html", context)
# 	else:
# 		return redirect('home')