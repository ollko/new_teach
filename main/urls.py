from django.conf.urls import url

from . import views
from models import Album

app_name = 'main'
urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^news/$', views.news, name='news'),
    url(r'^oge/$', views.oge, name='oge'),
    
    url(r'^fotoalbums/$', views.fotoalbums, name='fotoalbums'),
    url(r'^fotostring/$', views.fotostring, name='fotostring'),
    url(r'^fotofavorite/$', views.fotofavorite, name='fotofavorite'),
    url(r'^fotoalbums/new$', views.fotoalbums_new, name='fotoalbums_new'),
	url(r'^foto/(?P<album_id>[0-9]+)/$', views.foto_from_album, name='foto_from_album'),
	url(r'^foto/(?P<album_id>[0-9]+)/del/$', views.foto_from_album_del, name='foto_from_album_del'),
    
    url(r'^video/$', views.video, name='video'),
    url(r'^newproject/$', views.newproject, name='newproject'),
    url(r'^thanks/$', views.thanks, name='newproject'),

    url(r'^login/',"django.contrib.auth.views.login",
        {"template_name":"main/login.html",
        "extra_context":{"albs":Album.objects.all()}},
        name="login"),
    url(r'^logout/',"django.contrib.auth.views.logout",
        {"template_name":"main/logout.html",
        "extra_context":{"albs":Album.objects.all()}},
        name="logout"),

]