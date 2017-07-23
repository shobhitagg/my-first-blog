from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_redirect, name='home_redirect'),
    url(r'^home/$', views.home, name='home'),
	url(r'^members/$', views.members, name='members'),
	url(r'^guest/$', views.guest, name='guest'),
]
