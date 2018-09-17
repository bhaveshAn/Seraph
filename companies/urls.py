from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'all/', views.all, name='all'),
    url(r'^new/', views.new, name='new'),
    url(r'^(?P<id>[0-9]+)/', views.read, name='read'),
    url(r'^edit/(?P<id>[0-9]+)/', views.edit, name='edit'),
    url(r'^delete/(?P<id>[0-9]+)/', views.delete, name='delete'),
]
