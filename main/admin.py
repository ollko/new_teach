from django.contrib import admin

# Register your models here.
from .models import Event, Fotogalery

admin.site.register(Event)
admin.site.register(Fotogalery)