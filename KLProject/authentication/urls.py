"""
Handles all the urls. Take it as a list containing all the names of the different pages.
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#declaring name of app
app_name = 'authentication'

urlpatterns = [	
	#/authentication/login/
	#path('login/', views.user_login, name='login'),

	path('login/', auth_views.login, name='login'),

	path('logout/', auth_views.logout, name='logout'),

	path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),

	#/authentication/dashboard/
	path('', views.dashboard, name='dashboard'),

]
