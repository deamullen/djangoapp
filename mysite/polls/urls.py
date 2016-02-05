from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'polls'
urlpatterns = [
		url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^around-the-world/', views.world, name='world'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
