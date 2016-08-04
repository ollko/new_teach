# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AddVideoForm

from videos.models import Video

# Create your views here.
def  videos(request):
	content=Video.objects.all()

	return render (request, 'video/video.html',{'content':content})
	# return HttpResponse("Hello, world. You're at the VIDEO index.")

@permission_required('videos.add_video')
@login_required
def video_new(request):
	if request.method=='POST':
		form=AddVideoForm(request.POST)
		if form.is_valid():

			title=form.cleaned_data['title']
			video_html_code=form.cleaned_data['video_html_code']
			pub_date=timezone.now().date()
			v=Video(title=title,
				video_html_code=video_html_code,
				pub_date=pub_date)
			v.save()
			v.catch_youtube_id()
			v.save()
		return HttpResponseRedirect('/thanks/')

	else:
		form=AddVideoForm()

	return render(request, 'common/blank_for_adding.html', {'form': form,
					    	'title':'добавление нового видео',
					    	'value':'добавить видео'
					    	})

@permission_required('videos.delete_video')
@login_required	
def video_del(request):
	content=Video.objects.all()
	print "content=",content

	if request.method=='POST':
		
		for v in content:
			if unicode(v.id) in request.POST:
				
				v.delete()

		return HttpResponseRedirect('/thanks/')
				

	return render (request, 'video/video_del.html',{'content':content})


def thanks(request):
	return render (request, 'common/thanks.html',{'context':'видео'})
	
