# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Tests18_26,UserAnswer
from .forms import AddTests18_26Form
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

def listId():
	'''создает список из полей id модели Tests18_26'''
	tests=Tests18_26.objects.all()
	res=[]
	for test in tests:
		print 'test.id=',test.id
		res.append(test.id)
	return res

def nextTestId(test_id):
	'''принимает test_id в виде строки 
	и возвращает id в виде строки следующего теста18_26'''
	list_of_id=listId()
	if len(list_of_id)>1:

		next_index=list_of_id.index(int(test_id))+1
		print 'next_index=',next_index
		if next_index==len(list_of_id):

			return str(list_of_id[0])
		else:
			print 'type(str(list_of_id[next_index]))=',type(str(list_of_id[next_index]))
			return str(list_of_id[next_index])
	else:
		return None

def testListForUser(user):
	"""определяет список доступных тестов с результатами
	для авторизованного ученика"""
	available_tests_list = Tests18_26.objects.filter(answer__isnull=False)
	
	res=[]
	for test in available_tests_list:		
		a1=UserAnswer.objects.filter(user=user)
		a2=a1.filter(test18_26=test)
		if a2:
			res.append([test,a2[0].res,])
		else:
			res.append([test,'',])
	return res

def testListForMe():
	"""определяет список всех тестов (с ответами и без ответов),
	используется придобавлении ответов учителем"""

	res = Tests18_26.objects.all()
	return res

def testListAnonymous():
	res = Tests18_26.objects.filter(answer__isnull=False)
	return res


def parseTestText(test_id):
	test=Tests18_26.objects.get(id=test_id)
	test_all=test.tests18_26
	test_reverse=test.splited_tests18_26.split('-**-')
	test_reverse.reverse()
	test_list=[]
	while len(test_reverse)>=3:
		t, test_reverse = three_out(test_reverse)
		test_list.append(t)
	'''test_list=[[первая часть предложения, 
					начальная форма слова, 
					вторая часть предложения]  ,...]'''
	
	return test_all, test_list


# Create your views here.
def my_materials(request):
	return render(request,'oge/my_materials/my_materials.html')

def fipi(request):
	PERMS={ u'oge.add_tests18_26',u'oge.add_useranswer',
			u'oge.change_tests18_26',u'oge.change_useranswer',
			u'oge.delete_tests18_26',u'oge.delete_useranswer'}
	print 'type(PERMS)=',type(PERMS)
	
	current_user=request.user
	all_permissions=current_user.get_all_permissions()
	print 'all_permissions=',all_permissions

	if PERMS<=current_user.get_all_permissions():
		print 'пользователь может редактировать tests18_26'
		test_list_me=testListForMe()
		return render(request,'oge/fipi.html',{'test_list_me':test_list_me})
	
	elif current_user.is_anonymous():
		print 'анонимный пользователь tests18_26'
		test_list_an=testListAnonymous()
		return render(request,'oge/fipi.html',{'test_list_an':test_list_an})

	else:
		test_list_user=testListForUser(current_user)
		print 'зарегистрированный пользователь'
		print 	'test_list_user=',test_list_user
		return render(request,'oge/fipi.html',{'test_list_user':test_list_user})



def listening(request):
	return render(request,'oge/listen.http')

def reading(request):
	return render(request,'oge/listen.http')


@login_required
@permission_required('oge.add_tests18_26')

def my_test18_26_add (request):
	"""добавляет новую запись в Tests18_26,
	перенаправляет на сообщение об успешном добавлении нового задания """
	
	if request.method=='POST':
		form=AddTests18_26Form(request.POST)
		
		if form.is_valid():
			
			tests18_26=form.cleaned_data['tests18_26']
			current_date=timezone.now().date()

			t=Tests18_26(tests18_26=tests18_26)
			
			t.save()
			t.spliting()
			t.save()
			
			test_id = t.id
			return HttpResponseRedirect('/oge/fipi/my/test18_26/add/'+str(test_id)+'/thanks/')

	else:
		form=AddTests18_26Form()
		test_list_me = testListForMe()
	return render(request, 'oge/my_add_test18_26.html', {'form': form,
															'title':'скопируйте в это поле текст теста c сайта fipi.ru',
															'value': 'добавить',
															'test_list_me':test_list_me})			    	
def my_test18_26_add_thanks(request, test_id):
	"""отображает страницу 'новое задание успешно добавлено'"""
	
	test_list_me = testListForMe()

	return render(request,'oge/my_test18_26_add_thanks.html',
					{'test_id':test_id,'test_list_me':test_list_me})



def my_test18_26_blank(request, test_id):
	"""Вычисляет данные, для отображения пустого бланка
	одного теста из Test18_26 для для занесения правильных
	ответов учителем,
	также данные для отображения списка всех заданий 
	с указанием есть к ним ответы или нет"""


	test_all,test_list = parseTestText(test_id)

	t=Tests18_26.objects.get(id=test_id)
	ans=t.answer
	# если ответы уже есть добавим их к test_list для отображения в бланке
	# если пока нет, добавим к test_list ''
	if ans:		
		answer=ans.split('-**-')
		answer.reverse()
	else:
		answer=['' for x in range(int(t.qw_number))]

	for item in test_list:
		item.append(answer.pop())

	test_list_me = testListForMe()
	return render(request, 'oge/test18_26_detail.html',
	# test_all - тест целиком, как он заносится в поле для добавления нового теста учителем
	# test_list(с ответами если есть) - см. def parseTestText(test_id) выше
	# test_id - test_id
	# test_list_me=Tests18_26.objects.all()
		{'test_all': test_all,
		'test_list':test_list,
		'test_id':test_id,
		'test_list_me':test_list_me})


@permission_required('oge.add_tests18_26')
@login_required
def my_test18_26_add_answer(request,test_id):
	"""Добавляет ответы теста 18_26 в бд,
	перенаправляет на страницу 
	"ответ к тесту успешно добавлен" """
	
	t=get_object_or_404(Tests18_26, id=test_id)
	ans=request.POST
	l=len(ans)
	print 'ans=',ans
	answer = ['' for i in range(l-1) ]
	
	for x in range(1,l):
		answer[x-1]=ans[str(x)].strip().lower()

	a='-**-'.join(answer)
	t.answer= a
	t.save()

	return HttpResponseRedirect('/oge/fipi/my/test18_26/'+str(test_id)+'/add_answer/thanks/')

def my_test18_26_add_answer_thanks(request,test_id):
	"""отображает страницу 'ответ к тесту успешно добавлен'"""
	test_list_me = testListForMe()

	return render(request,'oge/my_test18_26_add_answer_thanks.html',
					{'test_id':test_id,'test_list_me':test_list_me})

def  pass_test18_26(request,test_id):
	"""добавляет ответ ученика в БД (модель UserAnswer) 
	и перенаправляет на страницу 
	'/oge/fipi/test18_26/<test_id>/check_answer/'  """

	user=request.user

	test18_26=get_object_or_404(Tests18_26, id=test_id)

	answer=test18_26.answer
	ans=answer.split('-**-')
	p=request.POST

	l=len(p)

	user_ans = ['' for i in range(l-1) ]
	
	for x in range(1,l):
		user_ans[x-1]=p[str(x)].strip().lower()
	# res - число правильных ответов пользователя в тесте
	res=0
	# res_number - строка из единиц и нулей (0 - неправильноб 1 - правильно) 
	res_numbers=''
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
	"""отображает бланк теста c ответами пользователя 
	(зеленый правильно, красный неправильно)"""

	test=Tests18_26.objects.get(id=test_id)

	test_all=test.tests18_26

	user_id=request.user.id
	
	useranswer=test.useranswer_set.get(user=user_id)
	print 'useranswer=',useranswer
	res_numbers=useranswer.res_numbers
	# получим лист из тройных элементов для отображения каждого предлодения теста
	test_splited=test.splited_tests18_26.split('-**-')
	test_splited.reverse()
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
	print 'test_list=',test_list
	'''test_list=[[начало предложения, ответ пользователя, конец предложения, правильный ответ,True or False],..
	]'''
	# Вывод всех доступных тестов с указанием степени пройденности для авторизованного учееника:
	user=request.user
	test_list_user=testListForUser(user)	
	
	return render(request, 'oge/cheсk_answer.html',
							{'test': test_all,
							'test_list':test_list,
							'test_id':test_id,
							'test_list_user':test_list_user})

def three_out(l):
	t=[]
	i=0
	while i<=2:
		t.append(l.pop())
		i=i+1

	return t,l


def test18_26_blank(request, test_id):
	"""Вычисляет данные,для отображения пустого бланка 
	одного теста из Test18_26 для заполнения учениками,
	также данные отображения списка доступных заданий 
	с результатами (например: пройдено 8 из 9)"""

	'''подготовим данные для отображения теста под номером test_id:
	 '''
	test_all,test_list = parseTestText(test_id)

	
	# Вывод всех доступных тестов с указанием степени пройденности для авторизованного учееника:

	user=request.user
	if user.is_anonymous():
		return render(request, 'oge/test18_26_blank.html',
							{'test_all': test_all,
							'test_list':test_list,
							'test_id':test_id,})
	else:	
		test_list_user=testListForUser(user)	
		
		return render(request, 'oge/test18_26_blank.html',
								{'test_all': test_all,
								'test_list':test_list,
								'test_id':test_id,
								'test_list_user':test_list_user})

def a_test18_26_blank(request, test_id):
	'''Вычисляет данные,для отображения пустого бланка 
	одного теста из Test18_26 для заполнения анонимным 
	пользователем,
	также данные отображения списка доступных заданий 
	для пользователя без регистрации	'''

	test_all,test_list = parseTestText(test_id)
	t=Tests18_26.objects.get(id=test_id)
	print 'test_id=',test_id
	print 'type(test_id)=',type(test_id)
	ans=t.answer
	answer=ans.split('-**-')
	answer.reverse()

	for item in test_list:
		item.append(answer.pop())

	'''test_list=[[начало предложения, 
					ответ пользователя, 
					конец предложения, 
					правильный ответ],   [...]]'''
	
	test_list_an = Tests18_26.objects.filter(answer__isnull=False)
	'''test_list_an - список тестов, 
	доступных для незарегистрированного пользователя'''
	
	test_id_int=int(test_id)
	next_test_id=nextTestId(test_id)
	return render(request, 'oge/a_test18_26_blank.html',
							{'test_all': test_all,
							'test_list':test_list,
							'test_id':test_id,
							'test_id_int': test_id_int,
							'next_test_id':next_test_id,
							'test_list_an':test_list_an})