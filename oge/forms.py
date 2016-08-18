from django.forms import ModelForm
from oge.models import Tests18_26

class AddTests18_26Form(ModelForm):
	class Meta:
		model = Tests18_26
		fields = ('tests18_26',)