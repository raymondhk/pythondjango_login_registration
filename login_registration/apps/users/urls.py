from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^success/$', success),
]
