# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tests18_26(models.Model):
	tests18_26 = models.TextField()

	def __unicode__(self):

		return u'tests18_26 №'+str(self.id)
