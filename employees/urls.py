from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(
        r'all/',
        views.all,
        name='all',
    ),
    url(
        r'^login/',
        views.auth_view,
        name='login',
    ),
    url(
        r'^logout/',
        auth_views.logout,
        name='logout',
        kwargs={'next_page': '/'},
    ),
    url(
        r'^register/',
        views.register,
        name='register',
    ),
    url(r'^profile/$', views.profile, name='profile'),
]
