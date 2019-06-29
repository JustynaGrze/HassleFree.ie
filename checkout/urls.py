from django.conf.urls import url
from .views import checkout, stripe

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^stripe/$', stripe, name='stripe'),
]