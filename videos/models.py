# coding=utf-8
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class VideoSection(models.Model):
	title=models.CharField(max_length=20,unique=True,verbose_name=u'раздел видео')
	
	def __unicode__(self):
		return self.title


class Video(models.Model):
	video_section=models.ForeignKey(VideoSection, default='1',on_delete=models.CASCADE,
		verbose_name=u'раздел')
	
	title=models.CharField(max_length=200,
							unique=True,
							verbose_name=u'название')
	video_html_code=models.CharField(max_length=200,
									default=None,
									verbose_name=u'html-код')
	pub_date=models.DateTimeField()
	youtube_id=models.CharField(max_length=11,null=True,blank=True,default=None)

	
	def __unicode__(self):
		return self.title

	def catch_youtube_id(self):
		
		pattern=re.compile(r'embed/([a-zA-Z0-9-_]{11})')
		self.youtube_id=pattern.findall(self.video_html_code)[0]

