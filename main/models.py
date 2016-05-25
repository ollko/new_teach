# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Album(models.Model):
	album = models.CharField(max_length=200,unique=True)
	album_date = models.DateField('album date')
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.album


class Foto(models.Model):
	album = models.ForeignKey(Album, verbose_name = u'Выберите из списка или введите новое название:', on_delete=models.CASCADE)
	foto = models.ImageField(u'Выберите фотофайл',upload_to = 'fotos/thumbnails/%Y/%m/%d')
	published_date = models.DateField()
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.foto.url

	def save(self,*args,**kwargs):
		try:
			this_record=Foto.objects.get(id=self.id)
			if this_record.foto !=self.foto:
				this_record.foto.delete(save=False)
		except:
			pass
		super(Foto,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.foto.delete(save=False)
		super(Foto,self).delete(*args,**kwargs)



