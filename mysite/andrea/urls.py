from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'andrea'
urlpatterns = [
		url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
