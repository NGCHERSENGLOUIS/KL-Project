"""
Handles all the urls. Take it as a list containing all the names of the different pages.
"""

from django.urls import path
from . import views
#Import Dashboard from Authentication App
import authentication

#declaring name of app
app_name = 'intakeForm'

urlpatterns = [
	
	#/Authentication/Dashboard/
	#path('', Authentication.views.dashboardView.as_view(), name='dashboard'),

]