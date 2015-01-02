from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'app.views.home', name='home'),
     url(r'^home2/$', 'app.views.home2', name='home2'),
     url(r'^post/(\d+)$', 'app.views.post', name='post'),
     url(r'^live/(\d+)/(\d+)$', 'app.views.live', name='live'),
     url(r'^request/$', 'app.views.request', name='request'),
     					
	
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
