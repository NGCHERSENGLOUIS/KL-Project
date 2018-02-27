from django import forms

#LoginForm will be used to authenticate users against the database.
class LoginForm(forms.Form):
	username = forms.CharField()
	#Use PasswordInput widget to render HTML input elememt, including a type="password" attribute
	password = forms.CharField(widget=forms.PasswordInput)
