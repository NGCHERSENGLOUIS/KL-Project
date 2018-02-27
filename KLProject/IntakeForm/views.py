from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView #CreateView creates objects, UpdateView updates...
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login #this module will take username and password and verify them in existing database, and attach a session id to allow them to browse through authorized pages during that session
from django.urls import reverse_lazy
#Import models
#from .models import AdminDetails



class DashboardView(generic.ListView):
	template_name = 'intakeForm/dashboard.html'

class AdminDetails(CreateView):
	#model = AdminDetails
	fields = []