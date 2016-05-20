from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="characters"),
    url(r'^(?P<character_id>[0-9]+)/$', views.view_character, name='content-view_character'),
    url(r'^$', views.superpowers, name="superpowers"),
    url(r'^$', views.weapons, name="weapons")
]
