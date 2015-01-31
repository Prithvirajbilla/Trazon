from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/request$','donor.views.item_request'),
    url(r'^post/trip$','donor.views.post_trip'),
    url(r'^items/1$','donor.views.item_view'),
    url(r'$','donor.views.home'),
)
