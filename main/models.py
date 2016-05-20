# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Event(models.Model):
	event = models.CharField('',max_length=200)

	event_data = models.DateField('data event happening')

	def __unicode__(self):
		return self.event


class Fotogalery(models.Model):
	event = models.ForeignKey(Event, verbose_name = u'Выберите из списка или введите новое мероприятие:', on_delete=models.CASCADE)
	name = models.CharField('Add foto title',max_length=200, default = '')

	foto = models.ImageField('Choose the fotofile',upload_to = 'fotos/thumbnails/%Y/%m/%d')


	def __unicode__(self):
		return self.name

	def save(self,*args,**kwargs):
		try:
			this_record=Fotogalery.objects.get(id=self.id)
			if this_record.foto !=self.foto:
				this_record.foto.delete(save=False)
		except:
			pass
		super(Fotogalery,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.foto.delete(save=False)
		super(Fotogalery,self).delete(*args,**kwargs)



