# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tests18_26(models.Model):
	tests18_26 = models.TextField()

	def __unicode__(self):

		return u'tests18_26 №'+str(self.id)

class Answer(models.Model):
	test = models.ForeignKey(Tests18_26, on_delete=models.CASCADE)
	user = models.ForeignKey(User,)
	answer = models.CharField()
