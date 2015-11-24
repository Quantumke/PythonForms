from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context
from django.template import RequestContext, loader
from rango.forms import register
# Create your views here.
def reg(request):
	#Getting the context from request
	context = RequestContext(request)
#checking in request is a post
	if request.method=='POST':	
		form = register(request.POST)

		if form.is_valid():
#if form is valid save the form
			form.save(commit=True)
#Redirect after success
			return index(request)
		else:
			print forms.errors
	else:
		form = register()
	return render_to_response('index.html', {'form':form}, context )
