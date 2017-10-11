# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from datetime import datetime
# from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from precise_bbcode.fields import BBCodeTextField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class New(models.Model):
	title = models.CharField(max_length = 100,unique_for_date = 'posted',
		verbose_name = "Заголовок")
	description = models.TextField(verbose_name = "Краткое содержание")
	content = models.TextField(verbose_name = "Полное содержание")
	posted = models.DateTimeField(auto_now_add=True,db_index = True,verbose_name = 'Дата и время создания')
	# is_commentable = models.BooleanField(default = True,
	# 	verbose_name = "Разрешены комментарии")
	# tags = TaggableManager(blank = True, verbose_name = "Теги")
	# user = models.ForeinKey(User, editable = False)

	# def get_absolute_url(self):
	# 	return reverse("news:news_detail", kwargs = {'pk': self.pk})
	image = ProcessedImageField(verbose_name = 'Картинка',
											help_text = "Будет лучше загрузить landscape фото ",
											upload_to='new_image',
											processors= [ResizeToFill(450,300)],
											format='JPEG',
											options={'quality': 60},)
	def __unicode__(self):
		return self.title
		
	class Meta:
		ordering = ["-posted"]
		verbose_name = "новостная статья"
		verbose_name_plural = "новостные статьи"

	def delete(self, *args, **kwargs):
	    self.image.delete(save = False)
	    super(New, self).delete(*args, **kwargs)

# from django.contrib.comments.moderation import CommentModerator, moderator

# class NewsModerator(CommentModerator):
# 	email_notification = True
# 	enable_field = 'is_commentable'
	
# moderator.register(News,NewsModerator)


		
