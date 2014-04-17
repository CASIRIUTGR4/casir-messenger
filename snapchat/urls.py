from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^dashboard/$', 'snapchat.views.dashboard', name="dashboard"),
    url(r'^presentation/$', 'snapchat.views.presentation', name="presentation"),
)