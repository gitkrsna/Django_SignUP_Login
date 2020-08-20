
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'first_name', 'last_name',]

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['phone',] 
