# coding=utf-8
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import FotogaleryForm
from main.models import Fotogalery, Event



# Create your views here.
#def index (request):
#	return HttpResponse('This is my MAIN app!!!')
def  mainpage(request):
	return render (request, 'main/mainpage.html')

def  about(request):
	return render (request, 'main/about.html')	

def  news(request):
	return render (request, 'main/news.html')	

def  oge(request):
	return render (request, 'main/oge.html')

def  fotostring(request):
	ten_fist_foto=Fotogalery.objects.order_by('-id')[:10]
	print 'ten_fist_foto=',ten_fist_foto
	context= {'ten_fist_foto':ten_fist_foto}
	return render (request, 'main/fotostring.html',context)

def fotoalbums(request):
	try:
		events=Event.objects.all()

	except Event.DoesNotExist:
		raise Http404(u"Пока в фотогалерею не добавлено ни одного фотоальбома :(")

	event_list=[]
	for event in events:
		event_list_item={}

		event_list_item['event_data']=event.event_data
		event_list_item['event']=event.event
		event_id = event.id
		event_list_item['id']=event_id
		foto_from_event = Fotogalery.objects.filter(event_id = event_id)
		#print "event_id=", event_id
		#print "foto_from_event=",foto_from_event

		if  not foto_from_event:
			#print "foto_from_event=",foto_from_event
			event_list_item['foto']=u"не добавлено ни одного фото"
		else:

			s=foto_from_event[0]
			d=s.foto
			print 's=',s,"d=",d
			event_list_item['foto']=foto_from_event[0].foto

		event_list.append(event_list_item)


	print 'event_list=', event_list
	return render (request, 'main/fotoalbums.html',{"event_list": event_list})
	

def foto_from_event(request,event_id):
	event=Event.objects.get(id=event_id)
	#print "event=", event
	foto_from_event = Fotogalery.objects.filter(event_id = event_id)
	#print "foto_from_event=", foto_from_event

	content= {'foto_from_event':foto_from_event,'event':event}	
	return render (request, 'main/foto_from_event.html', content)
	
def foto_from_event_del(request,event_id):
	#Get list of foto with event_id=event_id
	fotos=Fotogalery.objects.filter(event_id=event_id)
	print 'fotos=', fotos
	if request.method=='POST':
		
		for foto in fotos:
			if unicode(foto.id) in request.POST:
				print 'request.POST[unicode(foto.id)]=',request.POST[unicode(foto.id)]
				print 'foto=',foto
				foto.delete()
				print 'foto=',foto
		return HttpResponseRedirect('/thanks/')
				
	else:
		content= {'foto_from_event':fotos, 'event_id':event_id}
		print "request.POST=",request.POST

	return render (request, 'main/foto_from_event_del.html', content)

	
def foto_new(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FotogaleryForm(request.POST,request.FILES)
        print "form = ", form
        # check whether it's valid:
        print form.is_valid()
        print form.errors
        if form.is_valid():
			# process the data in form.cleaned_data as required
			event = form.cleaned_data['event']
			name = form.cleaned_data['name']
			fotos = request.FILES

			print fotos.getlist('foto'), len(fotos.getlist('foto'))
			i=len(fotos.getlist('foto'))-1
			while i>=0:
				print 'foto=',fotos.getlist('foto')[i]
				foto = fotos.getlist('foto')[i]
				f = Fotogalery(event = event, name = name, foto= foto)
				f.save()
				i=i-1
				print f
            # redirect to a new URL:
			return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FotogaleryForm()
        print "print form"

    return render(request, 'main/foto_new.html', {'form': form})
	

def  video(request):
	return render (request, 'main/video.html')		

def  newproject(request):
	return render (request, 'main/newproject.html')	

def thanks(request):
	return render (request, 'main/thanks.html')
