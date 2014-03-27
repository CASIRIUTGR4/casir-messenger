from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url("^$", "snapchat.views.index", name="index"),
    url("^dashboard", "snapchat.views.dashboard", name="dashboard")
)