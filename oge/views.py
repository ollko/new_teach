# coding=utf-8
from django.shortcuts import render
from .models import Tests18_26
from .forms import AddTests18_26Form
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def my_materials(request):
	return render(request,'oge/my_materials/my_materials.html')

def fipi(request):
	return render(request,'oge/fipi.html')

def listening(request):
	return render(request,'oge/listen.http')

def reading(request):
	return render(request,'oge/listen.http')

def test18_26(request):
	latest_tests18_26_list = Tests18_26.objects.order_by('-pub_data')[:5]
	context = {'latest_tests18_26_list': latest_tests18_26_list}
	return render(request, 'oge/test18_26.html', context)

@permission_required('oge.add_test18_26')
@login_required
def new (request):
	if request.method=='POST':
		form=AddTests18_26Form(request.POST)
		
		if form.is_valid():
			
			tests18_26=form.cleaned_data['tests18_26']
			current_date=timezone.now().date()

			t=Tests18_26(tests18_26=tests18_26)
			
			t.save()
			t.spliting()
			t.save()
			
			return HttpResponseRedirect('/thanks/add_tests18-26/')

	else:
		form=AddTests18_26Form()

	return render(request, 'common/blank_for_adding.html', {'form': form,
															'title':'добавьте новый тест:',
															'value': 'добавить'				    	
					    	})

def three_out(l):
	t=[]
	i=0
	while i<=2:
		t.append(l.pop())
		i=i+1

	return t,l


def test18_26_detail(request, test_id):
	# Получаем нужную запись из БД:
	test=Tests18_26.objects.get(id=test_id)

	test_all=test.tests18_26

	test_reverse=test.splited_tests18_26.split('-**-')
	test_reverse.reverse()
	print 'test_reverse=',test_reverse
	print 'len(test_reverse)=',len(test_reverse)
	test_list=[]
	while len(test_reverse)>=3:
		t, test_reverse = three_out(test_reverse)
		print 't=',t
		print 'test_reverse=',test_reverse
		test_list.append(t)

	print 'test_list[0]=',test_list[0]
	test_id=test.id
	
	return render(request, 'oge/test18_26_detail.html',
		{'test': test_all,'test_list':test_list,'id':test_id})
	