from django.db import models

class category(models.Model):
	name=models.CharField(max_length=20,default="")
	desc=models.TextField(default="")
	image = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	id_inc = models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=20,default="")
	category=models.CharField(max_length=20,default="")
	name=models.CharField(max_length=20,default="")
	desc=models.TextField(default="")
	contact_email=models.EmailField(default="")
	contact_phone=models.IntegerField(default=0)
	address=models.TextField(default="")
	image = models.ImageField(null=True, blank=True)
	price=models.IntegerField()
	def __str__(self):
		return self.name

class pending(models.Model):
	id_inc = models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=20,default="")
	category=models.CharField(max_length=20,default="")
	name=models.CharField(max_length=20,default="")
	desc=models.TextField(default="")
	contact_email=models.EmailField(default="")
	contact_phone=models.IntegerField(default=0)
	address=models.TextField(default="")
	image = models.ImageField(null=True, blank=True)
	price=models.IntegerField()
	def __str__(self):
		return self.name