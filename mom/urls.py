# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'mom'

urlpatterns = [
	url(r'^$', views.MomStuffList.as_view(), 
						    	name='momstuff_list',),

	url(r'^add/$', views.MomStuffCreate.as_view(), name = "mumstuff_add"),
	

	url(r'^(?P<pk>\d+)/update/$', views.MomStuffUpdate.as_view(), 
						    	name='momstuff_update',),

	url(r'^(?P<pk>\d+)/delete/$', views.MomStuffDelete.as_view(), 
								name='momstuff_delete',),

]