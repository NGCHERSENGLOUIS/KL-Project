from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
	if request.method == 'POST':

		#Create form instance with submitted data
		form = LoginForm(request.POST)

		#Check is form is valid
		if form.is_valid():
			#normalize data to a consistent format. 
			cd = form.cleaned_data
			#authenticate user against database
			user = authenticate(username=cd['username'], password=cd['password'])

			if user is not None:
				#Check if user is active
				if user.is_active:
					#log user into website
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			
			else:
				return HttpResponse('Invalid login')

	else:
		form = LoginForm()

	return render(request, 'authentication/login.html', {'form': form})


@login_required #Check if user is authenticated
def dashboard(request):
	return render(request, 'authentication/dashboard.html', {'section': 'dashboard'})

