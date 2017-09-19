# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save

# Create your models here.
from .utils import unique_slug_generator

def layout_validator(value):
	if value[0]  != '#':
		raise ValidationError('Должно начинаться с #')
	if len(value) == 4 or len(value) ==7:
		return value
	raise ValidationError('Некорректная длина')

class Baner(models.Model):
	title 				 = models.CharField(max_length=220)
	title_description	 = models.TextField(blank=True, null=True)
	jumbotron_bg_color	 = models.CharField(max_length = 7, default = '#000000', validators = [layout_validator])
	jumbotron_bg_img	 = models.ImageField(blank=True, null=True, upload_to = 'fotos')
	title_btn 			 = models.CharField(max_length=50, default='Join')
	title_btn_url		 = models.CharField(max_length=50, default='Join')
	content1 			 = models.TextField(blank=True, null=True)
	content2 			 = models.TextField(blank=True, null=True)
	content3 			 = models.TextField(blank=True, null=True)
	content4 			 = models.TextField(blank=True, null=True)
	content5 			 = models.TextField(blank=True, null=True)
	content6 			 = models.TextField(blank=True, null=True)
	
	video_embed 		 = models.TextField(null=True, blank=True) 
	slug 				 = models.SlugField(default='page-slug', blank=True)
	featured 			 = models.BooleanField(default=False)
	active 				 = models.BooleanField(default=True)
	leave_capture 		 = models.BooleanField(default=True)