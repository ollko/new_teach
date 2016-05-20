from django import forms
from .models import Fotogalery, Event
from .widgets import MultiFileInput

class FotogaleryForm(forms.ModelForm):

	class Meta:
		model = Fotogalery
		fields = ('event','foto','name',)
		widgets = {'foto':MultiFileInput}