# coding=utf-8
from django.conf.urls import url
from django.contrib.flatpages import views
from django.contrib.auth import views as auth_views
from . import views as my_views
from models import Album
from django.contrib.auth.decorators import permission_required

app_name = 'main'
urlpatterns = [

    url(r'^$', my_views.mainpage, name='mainpage'),
    
    url(r'^about/$', views.flatpage, {'url':'/about/'}),

    url(r'^news/$', my_views.news, name='news'),
    
    url(r'^fotoalbums/$', my_views.fotoalbums, name='fotoalbums'),
  

    url(r'^newproject/$', my_views.newproject, name='newproject'),
    

    url(r'^fotostring/$', my_views.fotostring, name='fotostring'),
    url(r'^fotofavorite/$', my_views.fotofavorite, name='fotofavorite'),
    url(r'^foto/(?P<album_id>[0-9]+)/$', my_views.foto_from_album, name='foto_from_album'),

    url(r'^fotoalbums/new$', my_views.fotoalbums_new, name='fotoalbums_new'),
	url(r'^foto/(?P<album_id>[0-9]+)/del/$',
                                my_views.foto_from_album_del, name='foto_from_album_del'),
    url(r'^foto/(?P<album_id>[0-9]+)/add/$', 
                                my_views.foto_to_album_add, name='foto_to_album_add'),

    url(r'^thanks/([a-z_1268/-]{8,14})/([0-9]*)/*$', my_views.thanks, name='thanks'),

   
    url(r'^login/', auth_views.login,
        {"template_name":"main/login.html",
        "extra_context":{'title':'вход','value':'войти'}
        }, name='login'),

    url(r'^logout/', auth_views.logout,
        {"template_name":"main/logout.html"}, name='logout'),

    url(r'^registration/',my_views.registration, name='registration'), 

]