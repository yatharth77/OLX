from django.shortcuts import render

from django.shortcuts import render, redirect
from products.models import Product, pending
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def pending_post(request):
	if request.user.is_authenticated and request.user.is_superuser:
		qs=pending.objects.all()
		context={
			"qs":qs,
		}
		return render(request, "superuser/pending.html",context)
	else:
		return HttpResponseRedirect('../')


def approve(request, *args, **kwargs):
	if request.user.is_authenticated and request.user.is_superuser:
			id_inc=kwargs["id_inc"]
			qs=pending.objects.all()
			for obj in qs:
				# print(obj.id_inc)
				if int(obj.id_inc) == int(id_inc):
					# print("heyyyyy")
					new_obj=Product()
					new_obj.user_name=obj.user_name
					new_obj.category=obj.category
					new_obj.name=obj.name
					new_obj.desc=obj.desc
					new_obj.contact_email=obj.contact_email
					new_obj.contact_phone=obj.contact_phone
					new_obj.address=obj.address
					new_obj.image=obj.image
					new_obj.price=obj.price
					new_obj.save()
					obj.delete()
					return HttpResponseRedirect('../../pending')
					break
			return HttpResponseRedirect('../../pending')
	else:
		return HttpResponseRedirect('../../../')



def decline(request, *args, **kwargs):
	# print("hhiiii")
	if request.user.is_authenticated and request.user.is_superuser:
			id_inc=kwargs["id_inc"]
			# print(id_inc)
			qs=pending.objects.all()
			for obj in qs:
				# print(obj.id_inc)
				if int(obj.id_inc) == int(id_inc):
					obj.delete()
					return HttpResponseRedirect('../../pending')
					break
			return HttpResponseRedirect('../../pending')
	else:
		return HttpResponseRedirect('../../../')

def users(request):
	if request.user.is_superuser:	
		# print("-----------------Hllo-------------------")
		qs=User.objects.all()
		context = {
		"qs":qs,
		}
		return render(request, "superuser/all_users.html", context)
	return redirect('home')