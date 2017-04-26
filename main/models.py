# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
import PIL
import os.path
from new_teach.settings import BASE_DIR
from django.core.files import File
import os
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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
	foto = models.ImageField(u'Выберите фотофайл в формате .jpg или .jpeg',upload_to = 'fotos/%Y/%m')
	foto_1x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/%Y/%m')
	foto_2x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/%Y/%m')
	foto_3x = models.ImageField(null=True,default=None,
		upload_to = 'fotos/%Y/%m')
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
		
		self.foto_1x.delete(save=False)
		self.foto_2x.delete(save=False)
		self.foto_3x.delete(save=False)
		super(Foto,self).delete(*args,**kwargs)

	def del_initial_foto(self,*args,**kwargs):
		self.foto.delete(save=False)	


	def foto_1x_2x_3x(self):
		print u'beginning foto_1x_2x_3x'
		img=PIL.Image.open(self.foto.path)
		
		size=(((324,420),'_1x'),((648,840),'_2x'),((1296,1680),'_3x'))
		
		# django_like_files - list с тремя Django file-like objects
		django_like_files=[]

		# name - имя загруженного файла-изображения
		name=self.foto.name

		for item in size:
			# делаем копию нашего исходного PIL объекта:
			foto_copy=img.copy()
			# преобразуе с помощю PIL в нужный формат
			foto_copy.thumbnail(item[0], PIL.Image.ANTIALIAS)
			

			if name.find('.jpeg')>-1:
				new_name=name.replace('.jpeg',item[1]+'.jpeg')
			elif name.find('.JPG')>-1:
				new_name=name.replace('.JPG',item[1]+'.JPG')
			else:
				pass

			print 'new_name=',new_name

			# создаем объект StringIO -
			foto_copy_io = StringIO.StringIO()
			# запоминаем в него наш PIlовский foto_copy
			foto_copy.save(foto_copy_io, format='JPEG')

			#  создаем new Django file-like object, чтобы впоследствии запомнить его в 
			# ImageFild поле модели

			foto_copy_file = InMemoryUploadedFile(foto_copy_io, None, new_name, 'image/jpeg',
                                  foto_copy_io.len, None)	
			

			django_like_files.append(foto_copy_file)
			
		
		
		self.foto_1x=django_like_files[0]
		
		self.foto_2x=django_like_files[1]
		
		self.foto_3x=django_like_files[2]
		

	
	

		


