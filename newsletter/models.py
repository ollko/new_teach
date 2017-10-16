# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.core.exceptions import ValidationError
import re


CHECK_IN_DATAS = (('1','22–24.09.17'),('2','29.09–01.10.17'),('3','6–8.10.17'),('4','27–29.10.17'),('5','24–26.11.17'))

def tel_validator(tel):
	tel_reg=r'^\+*[0-9-()]{10,15}$'
	if not re.match(tel_reg, tel) :
		
		raise ValidationError('Введите корректный номер телефона')
	
	return tel
	

# Create your models here.
class Join(models.Model):
	
	parents_name  = models.CharField(max_length=100, default = 'Иванов Иван Иванович')
	child_name    = models.CharField(max_length=100, default = 'Иванов Иван Иванович')
	birth_data    = models.DateField()
	check_in_date = models.CharField(verbose_name = 'Выберите дату заезда:', max_length=15, choices= CHECK_IN_DATAS, default='5' )
	tel = models.CharField(max_length=16, default='1234567890', validators = [tel_validator])
	email = models.EmailField()	
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email