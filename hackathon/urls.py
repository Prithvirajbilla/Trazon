from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','donor.views.home'),
    url(r'^login$','donor.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/request$','donor.views.item_request'),
    url(r'^profile$','donor.views.profile'),
    url(r'^post/trip$','donor.views.post_trip'),
    url(r'^items/1$','donor.views.item_view'),
	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
)
