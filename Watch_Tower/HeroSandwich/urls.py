from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^characters/$', views.index, name="characters"),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.view_character, name='characters'),

    #url(r'^$', views.superpowers, name="superpowers"),
    url(r'^weapons/$', views.weapons, name="weapons"),
    url(r'^weapons/(?P<weapon_id>[0-9]+)/$', views.weapons, name='weapons')
]
