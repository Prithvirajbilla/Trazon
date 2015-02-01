from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from django_facebook.models import *
from donor.models import *
# Create your views here.

def home(request):
	template = "home.html"
	return render(request,template)

def test(request):
	template = "test.html"
	return render(request,template)

def item_request(request):
	template = "request.html"
	return render(request,template)

def post_trip(request):
	template = "post_travel.html"
	return render(request,template)

def item_view(request,uid):
	item = Item.objects.get(pk=uid)
	template = "item_page.html"
	tp = int(item.item_price) + int(item.reward_amount)
	iteml = ItemListing.objects.get(item_id=item)
	uid = iteml.user_id.get_profile();
	return render(request,template,{"item":item,"tp":tp,"uid":uid})

def login(request):
	template = "login.html"
	return render(request,template)

def signup(request):
	template = "signup.html"
	return render(request,template)

import random
def profile(request):
	template = "profile.html"
	uid = request.user.id
	fbu =  FacebookCustomUser.objects.get(pk=uid).get_profile()
	about_me = fbu.about_me
	dob = fbu.date_of_birth
	image = fbu.image
	name = fbu.facebook_name
	gender = fbu.gender
	rating = random.randint(1,50)*0.1
	if gender == "m":
		gender = "Male"
	else:
		gender = "Female"
	#print about_me,dob,image,name,gender
	return render(request,template,{'name':name, 'sex':gender, 'about_me': about_me, 'dob': dob, 'image':image, 'rating':rating })

from django.contrib.auth import logout

def logout_all(request):
	logout(request)
	return HttpResponseRedirect("/")

def next(request):
	return HttpResponseRedirect("/")