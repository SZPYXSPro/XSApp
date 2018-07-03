from django.conf.urls import url
from artapp.views import *

urlpatterns = [
    url(r'^index/$', index),
    url(r'^tags/$', add_tags),
    url(r'^list_tags/$', list_tags),
]
