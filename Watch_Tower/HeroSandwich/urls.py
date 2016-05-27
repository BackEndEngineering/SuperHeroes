from django.conf.urls import url
from . import views


app_name = 'characters'
urlpatterns = [
    url(r'^characters/$', views.index, name="characters"),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.view_character, name='view'),
    url(r'^description/$', views.description, name="description"),
    url(r'^description/(?P<description_id>[0-9]+)/$', views.view_description, name='description'),
    url(r'^weapons/$', views.weapons, name="weapons"),
    url(r'^weapons/(?P<weapon_id>[0-9]+)/$', views.weapons, name='weapons'),
    url(r'^contact/$', views.contact_form, name="contact_form"),
    url(r'^create/$', views.create_article_form, name="create")
]
