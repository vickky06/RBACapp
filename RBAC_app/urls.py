from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name = 'index'),
    url(r'^(?P<username>[0-9,a-z,A-Z]+)/password$', views.userID,name = 'userID'),
    url(r'^(?P<username>[0-9,a-z,A-Z]+)/password/form_upload/$', views.model_form_upload,name = 'model_form_upload'),
    url(r'^(?P<username>[0-9,a-z,A-Z]+)/password/proximitySearch$', views.proximitySearch,name = 'proximitySearch'),
    url(r'^(?P<username>[0-9,a-z,A-Z]+)/$', views.userEntry,name = 'userEntry'),
    
    url(r'admin/',admin.site.urls,name = 'admin'),
    
    
    
]
