# coding=utf-8
import datetime

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import AlbumForm, RegistrationForm
from main.models import Foto, Album
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
#def index (request):
#	return HttpResponse('This is my MAIN app!!!')
def mainpage(request):
	return render (request, 'main/mainpage.html',
		{"request": request})

def about(request):
	return render (request, 'main/about.html')	

def news(request):
	return render (request, 'main/news.html')	

def oge(request):
	return render (request, 'main/oge.html')

def fotostring(request):
	ten_fist_foto=Foto.objects.order_by('-id')[:10]
	print 'ten_fist_foto=',ten_fist_foto
	context= {'ten_fist_foto':ten_fist_foto}
	return render (request, 'main/fotostring.html',context)

def	fotofavorite(request):
	return render (request, 'main/fotofavorite.html')

def fotoalbums(request):
	try:
		albums=Album.objects.order_by('-album_date')
		print 'albums=',albums

	except Album.DoesNotExist:
		raise Http404(u"Пока в фотогалерею не добавлено ни одного фотоальбома :(")

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
			content_item['foto']=fotos[0].foto.url

		content.append(content_item)

	form = AlbumForm()

	return render (request, 'main/fotoalbums.html',{"content": content,
		'form': form})
	

def foto_from_album(request,album_id):
	album=Album.objects.get(id=album_id)
	print "album=", album.album
	foto_from_album = Foto.objects.filter(album_id = album_id)
	print "foto_from_album=", foto_from_album

	content= {'foto_from_album':foto_from_album,'album':album}	
	print content
	return render (request, 'main/foto_from_album.html', content)

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
		return HttpResponseRedirect('/thanks/')
				
	else:
		content= {'foto_from_album':fotos, 'album_id':album_id}
		print "request.POST=",request.POST

	return render (request, 'main/foto_from_album_del.html', content)

	
def fotoalbums_new(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST,request.FILES)
        # print "form = ", form
        # check whether it's valid:
        # print form.is_valid()
        # print form.errors
        if form.is_valid():
			# process the data in form.cleaned_data as required
			album = form.cleaned_data['album'].lower()
			album_date = form.cleaned_data['album_date']

			a=Album(album=album,album_date=album_date)
			a.save()
			print 'a=',a
			fotos = request.FILES
			# print 'fotos=', fotos

			# print fotos.getlist('fotos'), len(fotos.getlist('fotos'))
			i=len(fotos.getlist('fotos'))-1
			current_date=timezone.now().date()

			while i>=0:
				print 'foto=',fotos.getlist('fotos')[i]
				print 'current_date.__format__=',current_date.__format__
				foto = fotos.getlist('fotos')[i]
				published_date=current_date
				f = Foto(album =a, published_date = current_date, foto= foto)
				print 'type(a)=',type(a)
				print 'type(published_date)=',type(published_date)
				print 'type(foto)=',type(foto)
				f.save()
				
				f.foto_1x_2x_3x()
				print 'f.foto_1x.name=',f.foto_1x.name
				print 'f.foto_1x.url=',f.foto_1x.url
				print 'f.foto_1x.path=',f.foto_1x.path
				f.save()
				i=i-1
				print f
            # redirect to a new URL:
			return HttpResponseRedirect('/thanks/')
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

def thanks(request):
	return render (request, 'main/thanks.html')

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

			
			print 'form=',form

			user=User.objects.create_user(username,email,password)
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			return HttpResponseRedirect('/thanks/')
	else:	
		form=RegistrationForm()


	return render (request, 'main/form.html',
		{'form': form, 'title':'Регистрация','value':'зарегистрироваться'})

