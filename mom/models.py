# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class MomStuff(models.Model):

	title = models.CharField(max_length = 80, verbose_name = "Заголовок", unique_for_date = 'posted',)
	posted = models.DateTimeField(default=timezone.now, db_index = True, verbose_name = 'Время и дата загрузки')
	stuffFile = models.FileField(verbose_name = "Файл с материалами", upload_to = 'stuff_pdf/%Y/%m', null=True)

	def __unicode__(self):
		return self.title

	def delete(self, *args, **kwargs):
	    self.stuffFile.delete(save = False)
	    super(MomStuff, self).delete(*args, **kwargs)

	class Meta:
		ordering = ["-posted"]
		verbose_name = "материал для мам"
		verbose_name_plural = "материалы для мам"