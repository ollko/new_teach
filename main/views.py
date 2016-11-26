# coding=utf-8
import datetime
from django.utils import timezone

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import AlbumForm, RegistrationForm, FotoToAlbumForm
from main.models import Foto, Album
from django.utils import timezone

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
#def index (request):
#	return HttpResponse('This is my MAIN app!!!')
def mainpage(request):
	return HttpResponseRedirect('/about/')

def news(request):
	
	return render (request, 'main/news.html',)	

def fotostring(request):
	ten_fist_foto=Foto.objects.order_by('-id')[:10]
	print 'ten_fist_foto=',ten_fist_foto
	context= {'ten_fist_foto':ten_fist_foto}
	return render (request, 'main/foto/fotostring.html',context)

def	fotofavorite(request):
	return render (request, 'main/foto/fotofavorite.html')

def fotoalbums(request):
	try:
		albums=Album.objects.order_by('-album_date')
		print 'albums=',albums

	except Album.DoesNotExist:
		raise Http404(u"Пока в фотогалерею не добавлено ни одного фотоальбома :-(")

	content=[]
	for album in albums:
		content_item={}
		album_id=album.id
		fotos = Foto.objects.filter(album_id=album_id)

		content_item['id']=album_id
		content_item['album']=album.album
		content_item['date']=album.album_date
		content_item['count']=fotos.count()
		content_item['views']=album.views

		if  not fotos:
			#print "foto_from_album=",foto_from_album
			content_item['foto']=None
		else:
			content_item['foto_1x_url']=fotos[0].foto_1x.url
			
		content.append(content_item)
		print 'content=',content

	form = AlbumForm()

	return render (request, 'main/foto/fotoalbums.html',{"content": content})
	

def foto_from_album(request,album_id):
	album=Album.objects.get(id=album_id)
	# print "album=", album.album
	foto_from_album = Foto.objects.filter(album_id = album_id)
	# print "foto_from_album=", foto_from_album

	content= {'foto_from_album':foto_from_album,'album':album}	
	# print content
	return render (request, 'main/foto/foto_from_album.html', content)



@permission_required('main.delete_foto')
@login_required	
def foto_from_album_del(request,album_id):
	#Get list of foto with album_id=album_id
	fotos=Foto.objects.filter(album_id=album_id)
	print 'fotos=', fotos
	if request.method=='POST':
		
		for foto in fotos:
			if unicode(foto.id) in request.POST:
				print 'request.POST[unicode(foto.id)]=',request.POST[unicode(foto.id)]
				print 'foto=',foto
				foto.delete()


		return HttpResponseRedirect('/thanks/del_foto/'+album_id+'/')
				
	else:
		content= {'foto_from_album':fotos, 'album_id':album_id}
		print "request.POST=",request.POST

	return render (request, 'main/foto/foto_from_album_del.html', content)

@permission_required('main.add_foto')
@login_required	
def foto_to_album_add(request,album_id):
	# if this is a POST request we need to process the form data
	album = Album.objects.get(id=album_id)
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:	
		form = FotoToAlbumForm(request.POST, request.FILES)

		if form.is_valid():

			fotos = request.FILES

			i=len(fotos.getlist('fotos'))-1
			current_date=timezone.now().date()

			while  i>=0:
				foto = fotos.getlist('fotos')[i]
				published_date=current_date
				f = Foto(album =album, published_date = current_date, foto= foto)
				f.save()

				f.foto_1x_2x_3x()
				f.save()
				i=i-1

			# удаляем первоначальное фото большого размера:
			f.del_initial_foto()
			
			return HttpResponseRedirect('/thanks/add_foto/'+album_id+'/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form=FotoToAlbumForm()
		a=album.album

	return render(request,  'main/form.html', {'form': form,
				    	'title':u'добавление новых фото в фотоальбом :%s'%album.album,
				    	'value':'добавить фото',
				    	'enctype_atr':'multipart/form-data'
				    	})


@permission_required('main.add_foto')
@login_required		
def fotoalbums_new(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST,request.FILES)

        if form.is_valid():
			# process the data in form.cleaned_data as required
			album = form.cleaned_data['album'].lower()
			album_date = form.cleaned_data['album_date']

			a=Album(album=album,album_date=album_date)
			a.save()
			print 'a=',a
			fotos = request.FILES

			i=len(fotos.getlist('fotos'))-1
			current_date=timezone.now().date()

			while i>=0:

				foto = fotos.getlist('fotos')[i]
				published_date=current_date
				f = Foto(album =a, published_date = current_date, foto= foto)

				f.save()
				
				f.foto_1x_2x_3x()

				f.save()
				i=i-1

			# удаляем первоначальное фото большого размера:
			f.del_initial_foto()

			return HttpResponseRedirect('/thanks/add_album/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()


    return render(request,  'main/form.html', {'form': form,
					    	'title':'добавление нового альбома',
					    	'value':'добавить альбом',
					    	'enctype_atr':'multipart/form-data'
					    	})
	

def  video(request):
	return render (request, 'main/video.html')		

def  newproject(request):
	return render (request, 'main/newproject.html')	

def thanks(request,*args):
	
	v = {

	'add_video':
				[u'видео успешно добавлено :)',u'вернуться на страницу видео?','/videos/',],
	'del_video':
				[u'видео успешно удалено :(',u'вернуться на страницу видео?','/videos/',],	
	'add_foto':
				[u'фото успешно добавлено :)',u'вернуться на страницу текущего альбома?',],
	'del_foto':
				[u'фото успешно удалено :(',u'вернуться на страницу текущего альбома?',],
	'add_album':
				[u'альбом успешно добавлен :)',u'вернуться на страницу фотоальбомы?',"/fotoalbums/",],
	'del_album':
				[u'альбом успешно удалён :(',u'вернуться на страницу фотоальбомы?',"/fotoalbums/",],
	'add_tests18-26':
				[u'добавлен очередной тест№№18-26 :)',u'проверить, что получилось?','/oge/',],


	}
	print "request.path=",request.path
	print 'args=',args
	print 'request.GET=',request.GET
	# print 'album_id=',album_id
	content=v[args[0]]
	print 'content=',content
	print "type(content[0]=)",type(content[0])

	

	

	if args[1] != '':

		content.append('/foto/'+args[1]+'/')
		print 'content=',content

	return render (request, 'common/thanks.html', {'content':content})


def registration (request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			print "form.is_valid()=",form.is_valid()

			username=form.cleaned_data['first_name']
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			email=form.cleaned_data['email']
			password=form.clean_password2()

			user=User.objects.create_user(username,email,password)
			user.first_name=first_name
			user.last_name=last_name
			user.save()

			new_user = authenticate(username=username, password=password)

			login(request, new_user)
		
			return HttpResponseRedirect('/')
	else:	
		form=RegistrationForm()
		return render (request, 'main/registration.html',
			{'form': form})

