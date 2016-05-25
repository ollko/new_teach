# coding=utf-8
from django import forms
from .models import Foto, Album
from .widgets import MultiFileInput


class AlbumForm(forms.Form):
	
	album = forms.CharField(label=u'название:', max_length=30)
	album_date = forms.DateField(label=u'выберите дату, кот.будет отображаться вместе с названием альбома:',
		widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),))
	fotos = forms.ImageField(label=u'выберите фотографии:', widget = MultiFileInput)
			
	
