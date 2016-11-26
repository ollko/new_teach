# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AddVideoForm
from django.core.urlresolvers import reverse

from videos.models import Video, VideoSection

# Create your views here.

def  videos(request,section_id):

	video_section=VideoSection.objects.get(id = section_id)
	videos = video_section.video_set.all()
	return render (request, 'video/video.html',{'video_section':video_section,
												'videos':videos})

@permission_required('videos.add_video')
@login_required
def video_new(request,section_id):
	if request.method=='POST':
		form=AddVideoForm(request.POST)
		if form.is_valid():

			title=form.cleaned_data['title']
			video_html_code=form.cleaned_data['video_html_code']
			video_section=form.cleaned_data['video_section']
			pub_date=timezone.now().date()
			v=Video(title=title,
				video_html_code=video_html_code,
				pub_date=pub_date,
				video_section=video_section)
			v.save()
			v.catch_youtube_id()
			v.save()
		return HttpResponseRedirect(reverse('videos:videos',kwargs={'section_id':section_id}))

	else:
		form=AddVideoForm()
		return_path=request.META.get('HTTP_REFERER','/')
	return render(request, 'video/blank_for_adding_video.html', {'form': form,
											'return_path': return_path})

@permission_required('videos.delete_video')
@login_required	
def video_del(request,section_id):
	video_section=VideoSection.objects.get(id = section_id)
	videos = video_section.video_set.all()

	if request.method=='POST':
		print 'request=POST'
		for v in videos:
			if unicode(v.id) in request.POST:
				
				v.delete()		
		return HttpResponseRedirect(reverse('videos:videos',kwargs={'section_id':section_id}))
				
	else:
		return render (request, 'video/video_del.html',
				{'video_section':video_section,'videos':videos})
