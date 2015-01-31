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

def post_trip(request):
	template = "post_travel.html"
	return render(request,template)

def item_view(request):
	template = "item_page.html"
	return render(request,template)

def login(request):
	template = "login.html"
	return render(request,template)

def profile(request):
	template = "profile.html"
	return render(request,template)