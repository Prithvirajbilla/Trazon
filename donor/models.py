from django.db import models

# Create your models here.

from open_facebook.api import OpenFacebook, FacebookAuthorization
from django.contrib.auth.models import User
from django_facebook.models import *

class Item(models.Model):
	name = models.CharField(max_length=100)
	item_price = models.CharField(max_length=100)
	reward_amount = models.CharField(max_length=100)
	available = models.CharField(max_length=100)
	item_description = models.TextField()
	photo = models.TextField(max_length=200)

	def __unicode__(self):
		return self.name

class Trip(models.Model):
	type_trip = models.CharField(max_length=100)
	origin = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	departure = models.CharField(max_length=100)
	arrival = models.CharField(max_length=100)


class ItemListing(models.Model):
	user_id = models.ForeignKey(FacebookCustomUser)
	item_id = models.ForeignKey(Item)

