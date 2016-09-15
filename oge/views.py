# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Tests18_26,UserAnswer
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

@login_required
@permission_required('oge.add_tests18_26')
def test18_26my(request):

	test_list = Tests18_26.objects.all()
	return render(request, 'oge/test18_26my.html', {'test_list': test_list})

@login_required
def test18_26(request):

	test_list = Tests18_26.objects.filter(answer__isnull=False)
	user=request.user
	test_list1=[]
	for test in test_list:		
		a1=UserAnswer.objects.filter(user=user)
		a2=a1.filter(test18_26=test)
		if a2:
			test_list1.append([test,a2[0].res,])
		else:
			test_list1.append([test,'',])
	print 'test_list1',test_list1

	return render(request, 'oge/test18_26.html', {'test_list': test_list1})



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
		answer[x-1]=ans[str(x)].lower()

	a='-**-'.join(answer)
	print 'a=',a
	print 'type(a)=',type(a)
	t.answer= a
	t.save()

	return HttpResponseRedirect('/oge/fipi/test18_26my/')

def  pass_test18_26(request,test_id):
	user=request.user

	test18_26=get_object_or_404(Tests18_26, id=test_id)

	answer=test18_26.answer
	ans=answer.split('-**-')
	p=request.POST

	l=len(p)

	user_ans = ['' for i in range(l-1) ]
	
	for x in range(1,l):
		user_ans[x-1]=p[str(x)].lower()
# res - число правильных ответов пользователя в тесте
	res=0
# res_number - строка из единиц и нулей (0 - неправильноб 1 - правильно) 
	res_numbers=''
	print 'ans=',ans
	print 'user_ans=',user_ans
	for (x,y) in zip(ans,user_ans):
		if x==y:
			res=res+1
			res_numbers=res_numbers+'1'
		else:
			res_numbers=res_numbers+'0'
	
	user_answer = '-**-'.join(user_ans)
	
	u=UserAnswer(user=user,test18_26=test18_26,
		user_answer=user_answer,res=str(res),res_numbers=res_numbers)
	u.save()

	return 	HttpResponseRedirect('/oge/fipi/test18_26/'+str(test_id)+'/check_answer/')


def check_answer(request,test_id):
	# отображает бланк теста c ответами пользователя (зеленый правильно, красный неправильно)
	test=Tests18_26.objects.get(id=test_id)

	test_all=test.tests18_26

	user_id=request.user.id
	
	useranswer=test.useranswer_set.get(user=user_id)
	print 'useranswer=',useranswer
	res_numbers=useranswer.res_numbers
# получим лист из тройных элементов для отображения каждого предлодения теста
	test_splited=test.splited_tests18_26.split('-**-')
	test_splited.reverse()
	# print 'test_reverse=',test_reverse
	# print 'len(test_reverse)=',len(test_reverse)
	user_answer=useranswer.user_answer.split('-**-')

	user_answer.reverse()

	test_list=[]
	i=0
	right_answer_reverse=test.answer.split('-**-')

	right_answer_reverse.reverse()

	while len(test_splited)>=3:
		t, test_splited = three_out(test_splited)
# заменим ЗАГОТОВКИ ответов ответами пользователя:
		print 'user_answer=',user_answer
		t[1]=user_answer.pop()
		t.append(right_answer_reverse.pop())
# добавим к списку t 4й элемент в виде True, если пользователь дал правильный ответ
		if res_numbers.startswith('1',i):
			t.append(True)
		i=i+1

		test_list.append(t)

	# print 'test_list[0]=',test_list[0]
	
	return render(request, 'oge/cheсk_answer.html',
		{'test': test_all,'test_list':test_list,'test_id':test_id} )	

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
	test_list=[]
	while len(test_reverse)>=3:
		t, test_reverse = three_out(test_reverse)
		# print 't=',t
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

