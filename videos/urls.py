# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'videos'

urlpatterns = [
	url(r'^$', views.videos, name='videos'),
	url(r'^new/$', views.video_new, name='video_new'),
	url(r'^del/$', views.video_del, name='video_del'),


]