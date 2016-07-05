# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
import Image
import os.path
from new_teach.settings import BASE_DIR
from django.core.files import File

# Create your models here.
class Album(models.Model):
	album = models.CharField(max_length=200,unique=True)
	album_date = models.DateField('album date')
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.album


class Foto(models.Model):
	album = models.ForeignKey(Album, 
		verbose_name = u'Выберите из списка или введите новое название:',
		on_delete=models.CASCADE)
	foto = models.ImageField(u'Выберите фотофайл',upload_to = 'fotos/thumbnails/%Y/%m/%d')
	foto_1x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/thumbnails/%Y/%m/%d')
	foto_2x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/thumbnails/%Y/%m/%d')
	foto_3x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/thumbnails/%Y/%m/%d')
	published_date = models.DateField()
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.foto.name

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

	def foto_1x_2x_3x(self):
		print 
		img=Image.open(self.foto.path)
		foto_1x=img.copy()
		foto_2x=img.copy()
		foto_3x=img.copy()
		

		size_1x = 324,420
		size_2x = 648,840
		size_3x = 1296,1680

		
		foto_1x.thumbnail(size_1x, Image.ANTIALIAS)
		path=self.foto.path.replace('.jpeg','_1x.jpeg')
		foto_1x.save(path)
		file_data=open(path,'r')
		file_file=File(file_data)
		print 'file_data.closed',file_data.closed
		print 'file_file.closed',file_file.closed
		self.foto_1x=file_file
		os.remove(path)

		
		
		foto_2x.thumbnail(size_2x, Image.ANTIALIAS)
		path=self.foto.path.replace('.jpeg','_2x.jpeg')
		foto_2x.save(path)
		file_data=open(path,'r')
		file_file=File(file_data)
		self.foto_2x=file_file
		os.remove(path)

		foto_3x.thumbnail(size_3x, Image.ANTIALIAS)
		path=self.foto.path.replace('.jpeg','_3x.jpeg')
		foto_3x.save(path)
		file_data=open(path,'r')
		file_file=File(file_data)
		self.foto_3x=file_file
		os.remove(path)

		


