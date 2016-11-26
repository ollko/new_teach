from django.forms import ModelForm
from videos.models import Video

class AddVideoForm(ModelForm):
	class Meta:
		model=Video
		fields=['title','video_html_code','video_section']