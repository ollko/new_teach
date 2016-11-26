from django.contrib import admin

# Register your models here.
from .models import Video, VideoSection

admin.site.register(Video)
admin.site.register(VideoSection)