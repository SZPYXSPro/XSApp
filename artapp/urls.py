from django.conf.urls import url
from artapp import views

urlpatterns = [
    url(r'', views.index),
]
