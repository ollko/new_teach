# coding=utf-8
from django.shortcuts import render, get_object_or_404
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

@permission_required('oge.add_test18_26')
@login_required
def test18_26my(request):

	test_list = Tests18_26.objects.all()

	return render(request, 'oge/test18_26my.html', {'test_list': test_list})

@login_required
def test18_26(request):

	test_list = Tests18_26.objects.filter(answer__isnull=False)

	return render(request, 'oge/test18_26.html', {'test_list': test_list})



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

@permission_required('oge.add_test18_26')
@login_required
def add_answer(request,test_id):
	
	t=get_object_or_404(Tests18_26, id=test_id)
	ans=request.POST
	# if not (answer[u'1'] and answer[u'1'] and answer[u'1'] and
	# 	answer[u'1'] and answer[u'1'] and answer[u'1'] and
	# 	answer[u'1'] and answer[u'1'] and answer[u'1']):
	l=len(ans)

	answer = ['' for i in range(l-1) ]
	
	for x in range(1,l):
		answer[x-1]=ans[str(x)]

	a='-**-'.join(answer)
	print 'a=',a
	print 'type(a)=',type(a)
	t.answer= a
	t.save()

	return HttpResponseRedirect('/oge/fipi/test18_26my/')

def  pass_test18_26(request,test_id):

	t=get_object_or_404(Tests18_26, id=test_id)
	p=request.POST







def three_out(l):
	t=[]
	i=0
	while i<=2:
		t.append(l.pop())
		i=i+1

	return t,l


def test18_26_detail(request, test_id):
	# отображает пустой бланк одного теста test18_26
	test=Tests18_26.objects.get(id=test_id)

	test_all=test.tests18_26
	test_reverse=test.splited_tests18_26.split('-**-')
	test_reverse.reverse()
	# print 'test_reverse=',test_reverse
	# print 'len(test_reverse)=',len(test_reverse)
	test_list=[]
	while len(test_reverse)>=3:
		t, test_reverse = three_out(test_reverse)
		# print 't=',t
		# print 'test_reverse=',test_reverse
		test_list.append(t)

	# print 'test_list[0]=',test_list[0]
	test_id=test.id
	
	return render(request, 'oge/test18_26_detail.html',
		{'test': test_all,'test_list':test_list,'id':test_id})
	# brought,impressed,did,children,me,didn't know,fell,could,first

def test18_26_blank(request, test_id):
	# отображает пустой бланк одного теста test18_26
	test=Tests18_26.objects.get(id=test_id)

	test_all=test.tests18_26
	test_reverse=test.splited_tests18_26.split('-**-')
	test_reverse.reverse()
	# print 'test_reverse=',test_reverse
	# print 'len(test_reverse)=',len(test_reverse)
	test_list=[]
	while len(test_reverse)>=3:
		t, test_reverse = three_out(test_reverse)
		# print 't=',t
		# print 'test_reverse=',test_reverse
		test_list.append(t)

	# print 'test_list[0]=',test_list[0]
	test_id=test.id
	
	return render(request, 'oge/test18_26_blank.html',
		{'test': test_all,'test_list':test_list,'id':test_id})	

def pass_test(request,test_id):
	return HttpResponse('здесь проверяется задание №ы%s'%str(test_id))