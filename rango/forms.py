from django import forms
from rango import forms

class register(forms.ModelForm)

	username = forms.CharField(max_length=100)
	email = forms.CharField(max_length=100)
	school = forms.CharField(max_length=100)
	form = forms.CharField(max_length=100)
	date = forms.CharField(max_length=100)
	gender= forms.CharField(max_length=100)
	password=forms.CharField(max_length=100)
	class Meta:
		models = forms
		fields = ('username', 'email', 'school', 'form', 'date', 'gender', 'password')
