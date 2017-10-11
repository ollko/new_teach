# coding=utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from .models import MomStuff

from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



# Create your views here.
class MomStuffList(ArchiveIndexView):
	model = MomStuff
	date_field = "posted"
	template_name = 'mom/stufflist.html'
	paginate_by = 10
	allow_empty = True
	allow_future = True

class MomStuffCreate(SuccessMessageMixin, CreateView):
	model = MomStuff
	success_url = reverse_lazy("mom:momstuff_list")
	success_message = "Новый материал успешно добавлен"
	fields = '__all__'

class MomStuffUpdate(SuccessMessageMixin, UpdateView):
	model = MomStuff
	success_url = reverse_lazy("mom:momstuff_list")
	success_message = "Новый материал успешно изменен"
	fields = '__all__'

class MomStuffDelete(SuccessMessageMixin,DeleteView):
	model = MomStuff
	template_name = "mom/stufflist_conform_delete.html"
	success_url = reverse_lazy("mom:momstuff_list")
	def post(self, request, *args, **kwargs):
		messages.add_message(request, messages.SUCCESS, "Материал успешно удален")
		return super(MomStuffDelete, self).post(request, *args, **kwargs)