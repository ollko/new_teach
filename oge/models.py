# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
import re
from django.utils import timezone

# Create your models here.

class Tests18_26(models.Model):
	tests18_26 = models.TextField()
	splited_tests18_26 = models.TextField(null=True,blank=True,default=None)
	pub_data = models.DateTimeField('дата публикации',default=timezone.now)


	def __unicode__(self):

		return u'tests18_26 №'+str(self.id)

	def spliting(self):
		res=[]

		list1=re.split(r'_+',self.tests18_26)
		
		if list1[0].isupper():
			res.append('')
		else: 
			res.append(list1[0])
			list1.remove(list1[0])

		latest = list1.pop()

		for item in list1:
			if item.isupper():
				res.append(item)
			else:
				point=item.find('.')

				if item[point+1]=='”':
					point=point+1
				
				res.append(item[:point+1])
				res.append(item[point+1:])

		res.append(latest)

		self.splited_tests18_26 = '-**-'.join(res)
		
	
class Answer(models.Model):

	tests18_26=models.OneToOneField(Tests18_26,)
	answer=models.CharField(max_length=200,null=True,blank=True,default=None)

				





			

