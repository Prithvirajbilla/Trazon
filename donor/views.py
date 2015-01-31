from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound

# Create your views here.

def home(request):
	template = "home.html"
	return render(request,template)

def item_request(request):
	template = "request.html"
	return render(request,template)