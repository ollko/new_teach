# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'videos'

urlpatterns = [
	url(r'^(?P<section_id>[123])/$', views.videos, name='videos'),
	url(r'^(?P<section_id>[123])/new/$', views.video_new, name='video_new'),
	url(r'^(?P<section_id>[123])/del/$', views.video_del, name='video_del'),
]