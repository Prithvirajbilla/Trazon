from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','donor.views.home'),
    url(r'^login$','donor.views.login'),
    url(r'^signup$','donor.views.signup'),
    url(r'^logout$','donor.views.logout_all'),
    url(r'^test$','donor.views.test'),
    url(r'^next$','donor.views.next'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/request$','donor.views.item_request'),
    url(r'^profile$','donor.views.profile'),
    url(r'^post/trip$','donor.views.post_trip'),
    url(r'^items/(\d+)$','donor.views.item_view'),
	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
