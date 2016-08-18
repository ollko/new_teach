# coding=utf-8
from django.shortcuts import render
from .models import Tests18_26
from .forms import AddTests18_26Form
from django.http import HttpResponseRedirect

# Create your views here.

def  index (request):
	return render (request, 'oge/index.html')

def new (request):
	if request.method=='POST':
		form=AddTests18_26Form(request.POST)
		
		if form.is_valid():
			
			tests18_26=form.cleaned_data['tests18_26']
			
			t=Tests18_26(tests18_26=tests18_26)
			
			t.save()
			
			return HttpResponseRedirect('/thanks/add_tests18-26/')

	else:
		form=AddTests18_26Form()

	return render(request, 'common/blank_for_adding.html', {'form': form,
															'title':'добавьте новый тест:',
															'value': 'добавить'				    	
					    	})