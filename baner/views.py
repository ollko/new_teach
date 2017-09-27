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

	def form_valid(self, form):
		parents_name  = form.cleaned_data.get('parents_name')
		child_name    = form.cleaned_data.get('child_name  ')
		birth_data    = form.cleaned_data.get('birth_data')
		check_in_date = form.cleaned_data.get('check_in_date')
		tel           = form.cleaned_data.get('tel')
		email         = form.cleaned_data.get('email')
		timestamp         = form.cleaned_data.get('timestamp')

		# other thing with email
		return super(HomeView, self).form_valid(form)

class PageDetailView(DetailView):
	queryset  = Baner.objects.filter(active=True)
	model=Baner
	template_name = 'baner/baner.html'