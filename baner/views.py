# coding=utf-8
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

from .models import Baner
from newsletter.forms import JoinForm

class BanerView(SuccessMessageMixin,CreateView):
	template_name = 'baner/baner.html'
	form_class = JoinForm
	success_url=reverse_lazy("baner:baner")

	def get_context_data(self, *args, **kwargs):
		context = super(BanerView, self).get_context_data(*args, **kwargs)
		context['object']= Baner.objects.filter(featured=True).first()#.order_by('?').first()
		return context

	def get_success_message(self, cleaned_data):
		# print(cleaned_data)
		return 'Спасибо что присоединились к нам! Мы скоро свяжемся с Вами!'

	# def form_valid(self, form):
	# 	email = form.cleaned_data.get('email')
	# 	# other thing with email
	# 	return super(HomeView, self).form_valid(form)

class PageDetailView(DetailView):
	queryset  = Baner.objects.filter(active=True)
	model=Baner
	template_name = 'baner/baner.html'