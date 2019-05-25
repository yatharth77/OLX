from django.db import models

# Create your models here.
class category(models.Model):
	name=models.CharField(max_length=20,default="")
	desc=models.TextField(default="")
	image = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name