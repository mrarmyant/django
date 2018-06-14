from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<pk>\d+)/$', views.show),
    url(r'^(?P<pk>\d+)/edit/$', views.edit),
    url(r'^(?P<pk>\d+)/delete/$', views.destroy),

]