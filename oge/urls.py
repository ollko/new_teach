# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'oge'

urlpatterns = [
	url(r'^$', views.my_materials, name='my_materials'),

	url(r'^fipi/$',views.fipi, name='fipi'),

	url(r'^fipi/my/test18_26/add/$', views.my_test18_26_add, name='my_test18_26_add'),

	url(r'^fipi/my/test18_26/add/(?P<test_id>[0-9]+)/thanks/$', views.my_test18_26_add_thanks, name='my_test18_26_add_thanks'),

	url(r'^fipi/my/test18_26/(?P<test_id>[0-9]+)/$',
		views.my_test18_26_blank, name='my_test18_26_blank'),
	
	url(r'^fipi/my/test18_26/(?P<test_id>[0-9]+)/add_answer/$',
		views.my_test18_26_add_answer, name='my_test18_26_add_answer'),

	url(r'^fipi/my/test18_26/(?P<test_id>[0-9]+)/add_answer/thanks/$',
		views.my_test18_26_add_answer_thanks, name='my_test18_26_add_answer_thanks'),


	url(r'^fipi/test18_26/(?P<test_id>[0-9]+)/$',
		views.test18_26_blank, name='test18_26_blank'),

	url(r'^fipi/test18_26/(?P<test_id>[0-9]+)/pass_test/$',
		views.pass_test18_26, name='pass_test18_26'),

	url(r'^fipi/test18_26/(?P<test_id>[0-9]+)/check_answer/$',
		views.check_answer, name='check_answer'),


	url(r'^fipi/a/test18_26/(?P<test_id>[0-9]+)/$',
		views.a_test18_26_blank, name='a_test18_26_blank'),

]