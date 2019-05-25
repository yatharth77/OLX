from django import forms

from .models import Product, pending

class pendingForm(forms.ModelForm):
	class Meta:
		model = pending
		fields= [
			"user_name",
			"category",
			"name",
			"desc",
			"contact_email",
			"contact_phone",
			"address",
			"image",
			"price",
		]
		widgets = {
        'user_name': forms.TextInput(attrs={'readonly': True}),
    	}