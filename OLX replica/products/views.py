
from django.shortcuts import render, redirect
from products.models import Product, pending, category
from .forms import pendingForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	qs= category.objects.all()
	# print(qs)
	context = {
	"list":qs,
	}
	return render(request,"product/home.html",context)

def display(request, *args, **kwargs):
	# print(kwargs['category'])
	in_cat=kwargs['category']
	cat_list=category.objects.all()
	flag=0
	for cat in cat_list:
		if cat.name.casefold()==in_cat.casefold():
			flag=1
	if flag==0:
		return redirect('../')
	qs=Product.objects.all()
	context={
		"category":in_cat,
		"list":qs,
	}
	return render(request, "product/product.html",context)

def upload(request):
	if request.user.is_authenticated:
		form=pendingForm(request.POST or None, request.FILES or None, initial={'user_name': request.user.username})
		if request.method == 'POST':
			if form.is_valid():	
				instance=form.save(commit=False)
				instance.save()
				return HttpResponseRedirect('../')
		context={
		"form":form,
		}
		return render(request,"product/upload_item.html",context)
	else:
		return HttpResponseRedirect('../')

def profile(request):
	print("-----HIII-----")
	if request.user.is_authenticated:
		qs1= Product.objects.all()
		qs2= pending.objects.all()
		context={
		"qs1":qs1,
		"qs2":qs2,
		}
		return render(request, "product/profile.html", context)
	else:
		return redirect('home')

def delete_product(request, *args, **kwargs):
	if request.user.is_authenticated:
		status=kwargs["status"]
		id_inc=kwargs["id_inc"]
		# print(status,id_inc)
		if status=="pending":
			qs=pending.objects.all()
		else:
			qs=Product.objects.all()
		for obj in qs:
			if int(obj.id_inc)==int(id_inc):
				obj.delete()
				return HttpResponseRedirect('../../')
		qs1= Product.objects.all()
		qs2= pending.objects.all()
		context={
		"qs1":qs1,
		"qs2":qs2,
		}
		return HttpResponseRedirect('../../')
	else:
		return redirect('home')

