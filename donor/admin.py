from django.contrib import admin

# Register your models here.
from django_facebook.models import *
from donor.models import *

admin.site.register(FacebookCustomUser)
admin.site.register(Item)
admin.site.register(Trip)
admin.site.register(ItemListing)
