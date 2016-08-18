# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'oge'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new, name='new'),
	


]