from django.conf.urls import url

from . import views

app_name = 'baner'

urlpatterns = [

	url(r'^$', views.BanerView.as_view(), name='baner'), 
	# url(r'^api/email/join$', JoinCreateAPIView.as_view(), name='email-join'),
    url(r'^(?P<slug>[\w-]+)/$', views.PageDetailView.as_view(), name='page-detail'),

]