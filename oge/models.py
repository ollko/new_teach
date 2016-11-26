# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
import re
from django.utils import timezone

# Create your models here.

class Tests18_26(models.Model):
	tests18_26 = models.TextField('Cкопируйте в это поле текст теста c сайта fipi.ru:')
	splited_tests18_26 = models.TextField(null=True,blank=True,default=None)
	pub_data = models.DateTimeField('дата публикации',default=timezone.now)
	answer=models.CharField(max_length=100,blank=True,default=1)
	qw_number = models.CharField('число вопросов в тесте',null=True,max_length=1,default='')


	def __unicode__(self):

		return str(self.id)

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
		self.qw_number = str(len(res)/3)
		
class UserAnswer(models.Model):
	user = models.ForeignKey(User)
	test18_26 = models.ForeignKey(Tests18_26)
	user_answer = models.CharField(u'строка с ответами пользователя',max_length=100,
									null=True,
									blank=True,
									default=None)
	res=models.IntegerField(u'число правильных ответов',null=True,blank=True,default=None)	
	res_numbers = models.CharField(max_length=9,
									null=True,
									blank=True,
									default=None)
	answer_pub_data = models.DateTimeField('дата ответа',default=timezone.now)

	def __unicode__(self):

		return 	u'ответ пользователя '+str(self.user)+' на тест №'+str(self.test18_26)

	def save(self,*args,**kwargs):

		try: 
			old_record=UserAnswer.objects.get(user=self.user,test18_26=self.test18_26)
			if old_record:
				old_record.delete()
		except:
			pass
		super(UserAnswer, self).save(*args,**kwargs)



			

