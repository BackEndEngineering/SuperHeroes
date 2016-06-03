"""Watch_Tower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import HeroSandwich
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from HeroSandwich.api import UserViewSet, CharacterViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'character', CharacterViewSet)

urlpatterns = [
     url(r'^', include('django.contrib.auth.urls')),
     url(r'^$', views.index, name="index"),
     url(r'^omniverse/', include('HeroSandwich.urls')),
     url(r'^admin/', admin.site.urls),
     url(r'^api/', include(router.urls)),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
