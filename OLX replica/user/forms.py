from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from phonenumber_field.modelfields import PhoneNumberField
user_type= [
    ('prime', 'PRIME'),
    ('non prime', 'NON PRIME'),
    ]

class UserRegisterForm(UserCreationForm):
	email= forms.EmailField()
	phone= forms.CharField()
	user_type= forms.CharField(label='user_type', 
		widget=forms.Select(choices=user_type), initial="non prime", disabled=True)

	class Meta:
		model = User
		fields = ['username' , 'email' , 'phone' , 'password1', 'password2', 'user_type']
		widgets = {
        'user_type': forms.TextInput(attrs={'readonly': 'readonly'}),
    	}