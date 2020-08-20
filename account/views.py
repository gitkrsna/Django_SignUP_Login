 
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm, ProfileForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			profile_form = ProfileForm(request.POST)
			if form.is_valid() and profile_form.is_valid():
				user = form.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save() 

				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')


		else:	
			form = CreateUserForm()
			profile_form = ProfileForm()
		
		context = {'form':form, 'profile_form' : profile_form, }
		return render(request, 'register.html', context)

		

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
    template_name = "welcome.html"
	
    return render(request, template_name, {'prof': Profile.objects.all() })




	
