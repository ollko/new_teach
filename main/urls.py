# coding=utf-8
from django.conf.urls import url

from . import views
from models import Album
from django.contrib.auth.decorators import permission_required

app_name = 'main'
urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    
    url(r'^about/$', 'django.contrib.flatpages.views.flatpage',
        {'url':'/about/'},name='about'),

    url(r'^news/$', views.news, name='news'),
    
    url(r'^fotoalbums/$', views.fotoalbums, name='fotoalbums'),
  
    url(r'^newproject/$', views.newproject, name='newproject'),
    

    url(r'^fotostring/$', views.fotostring, name='fotostring'),
    url(r'^fotofavorite/$', views.fotofavorite, name='fotofavorite'),
    url(r'^foto/(?P<album_id>[0-9]+)/$', views.foto_from_album, name='foto_from_album'),

    url(r'^fotoalbums/new$', views.fotoalbums_new, name='fotoalbums_new'),
	url(r'^foto/(?P<album_id>[0-9]+)/del/$',
                                views.foto_from_album_del, name='foto_from_album_del'),
    url(r'^foto/(?P<album_id>[0-9]+)/add/$', 
                                views.foto_to_album_add, name='foto_to_album_add'),

    url(r'^thanks/([a-z_]{8,9})/([0-9]*)/*$', views.thanks, name='thanks'),



    url(r'^thanksfornewalbum/$', views.thanksfornewalbum, name='thanksfornewalbum'),
    

   
    url(r'^login/',"django.contrib.auth.views.login",
        {"template_name":"main/login.html"
        # ,"extra_context":{'title':'вход','value':'войти'}
        }, name='login'),

    url(r'^logout/',"django.contrib.auth.views.logout",
        {"template_name":"main/logout.html"}, name='logout'),

    url(r'^registration/',views.registration, name='registration'),


    

]