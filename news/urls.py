from django.conf.urls import url

from news.views import NewListView, NewDetailView, NewCreate, NewUpdate, NewDelete

app_name = 'news'
urlpatterns = [
	url(r'^$', NewListView.as_view(), name = "news_index"),
	url(r'^(?P<pk>\d+)/detail/$', NewDetailView.as_view(), name = "news_detail"),
	url(r'^add/$', NewCreate.as_view(), name = "news_add"),
	url(r'^(?P<pk>\d+)/edit/$', NewUpdate.as_view(), name = "news_edit"),
	url(r'^(?P<pk>\d+)/delete/$', NewDelete.as_view(), name = "news_delete"),
	]