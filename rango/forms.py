from django import forms
from rango.models import forms
from django import forms

class register(forms.Form):


	class Meta:
		models = forms
		fields = ('username', 'email', 'school', 'form', 'date', 'gender', 'password')
