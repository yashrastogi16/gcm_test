from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from push_notifications.views import *

router = routers.DefaultRouter()
router.register(r'GCMDevice',GCMDeviceViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learndjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gcmtest/',include(router.urls)),
    url(r'^$','loginapp.views.login', name='login'),
    url(r'^login/','loginapp.views.login',name='login'),
    url(r'^test/','loginapp.views.test',name='test'),
    url(r'^dashboard/','loginapp.views.dashboard', name='dashboard'),
    url(r'^register/','loginapp.views.register', name='register'),
    url(r'^logout/','loginapp.views.logout', name='logout'),
    url(r'^editprofile/(?P<id>[0-9]+)$','loginapp.views.editprofile',name='editprofile'),
    url(r'^changepassword/(?P<id>[0-9]+)$','loginapp.views.changepassword',name='changepassword'),
    url(r'^gcmdevice_list/','push_notifications.views.gcmdevice_list',name='gcmdevice_list'),
    url(r'^admin/', include(admin.site.urls)),

)
