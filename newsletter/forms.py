# coding=utf-8
from django import forms

from .models import Join

BIRTH_YEAR_CHOICES = ('2000', '2001', '2002')
CHECK_IN_DATAS = ('22–24.09.17','29.09–01.10.17','6–8.10.17','27–29.10.17','24–26.11.17')

class JoinForm(forms.ModelForm):

	parents_name = forms.CharField(label='',
			widget=forms.TextInput(
					attrs={
						'placeholder':'ФИО родителя',
						'class': 'form-control'
						}
					))
	child_name = forms.CharField(label='',
			widget=forms.TextInput(
					attrs={
						'placeholder':'ФИО Ребенка',
						'class': 'form-control'
						}
					))
	birth_data = forms.DateField(label='Дата рождения ребенка:',widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES,),
					)

	# check_in_date=forms.ChoiceField(widget=forms.Select(
					
	# 				),
	# 				)
	
	tel = forms.CharField(label='',
			widget=forms.TextInput(
					attrs={
						'placeholder':'контактный телефон',
						'class': 'form-control'
						}
					))
	email = forms.EmailField(label='',
			widget=forms.EmailInput(
					attrs={
						'placeholder':'Ваш Email',
						'class': 'form-control'
						}
					))
	class Meta:
		model = Join
		exclude  = ['timestamp']

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		print ('email=',email)
		qs = Join.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Такой email уже существует")
		return email