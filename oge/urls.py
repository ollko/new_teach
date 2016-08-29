# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'oge'

urlpatterns = [
	url(r'^$', views.my_materials, name='my_materials'),
	url(r'^fipi/$',views.fipi, name='fipi'),
	url(r'^fipi/test18_26/$',views.test18_26, name='test18_26'),
	url(r'^fipi/test18_26/new/$', views.new, name='test18_26_new'),
	url(r'^fipi/test18_26/(?P<test_id>[0-9]+)/$',
		views.test18_26_detail, name='test18_26_detail'),

]