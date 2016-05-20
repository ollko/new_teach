from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^news/$', views.news, name='news'),
    url(r'^oge/$', views.oge, name='oge'),
    url(r'^fotostring/$', views.fotostring, name='fotostring'),
    url(r'^fotoalbums/$', views.fotoalbums, name='fotoalbums'),
    url(r'^foto/new/$', views.foto_new, name='foto_new'),
	url(r'^foto/(?P<event_id>[0-9]+)/$', views.foto_from_event, name='foto_from_event'),
	url(r'^foto/(?P<event_id>[0-9]+)/del/$', views.foto_from_event_del, name='foto_from_event_del'),
    url(r'^video/$', views.video, name='video'),
    url(r'^newproject/$', views.newproject, name='newproject'),
    url(r'^thanks/$', views.thanks, name='newproject'),


]