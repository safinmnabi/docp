from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Person, Task
from .forms import  UserForm, PersonForm, TaskForm
from django.views.generic.list import ListView




def Signin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		pwd = request.POST.get('password')

		check_user = User.objects.filter(email=email, password=pwd)

		if check_user:
			request.session['user'] = email
			request.session['isLogged'] = True
			return redirect('Index')
		else:
			return HttpResponse('Please enter valid Username or Password.')
	else:
		request.session['isLogged'] = False
		if request.session['isLogged']:
			return redirect('Signin')
		else:
			return render(request, 'Signin.html' )

def Signup(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		if User.objects.filter(email=email).count()>0:
			# messages.info(request, 'Email already exists.')
			return render(request, "signup.html", {'messages':'Email already exists.','status':'error'})
		else:
			user = User(email=email, password=password)
			user.save()
			return redirect('Signin')
	return render(request, "signup.html")

def Signout(request):
	try:
		del request.session['isLogged']
		request.session['isLogged'] = False
	except:
		return redirect('Signin')
	return redirect('Signin')


def Index(request):
	form = Person.objects.all().filter(eid=request.session['user'])
	return render(request, "crud.html", {'data':form, 'eid':request.session['user']})

def Datacreate(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		form.save()
		return redirect('Index')

	return render(request, 'add.html', {'eid':request.session['user']})

def Update(request, id):
	sel = Person.objects.get(id=id)
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=sel)
		form.save()
		return redirect('Index')
	else:
		form = PersonForm(instance=sel)
	return render(request, 'add.html', {'form': sel, 'eid':request.session['user']})

def Delete(request, id):
	sel= Person.objects.get(id=id)
	sel.delete()
	return redirect('Index')

def Taskdetail(request, id):
	sel= Task.objects.all().filter(pid=id)
	return render(request, 'taskdetail.html', {'data': sel, 'pid' : id})

def Taskcreate(request, id):
	if request.method == 'POST':
		pid = request.POST.get('pid')
		task = request.POST.get('taskname')
		form = TaskForm(request.POST)
		form.save()
		return redirect('Taskdetail', id)
	return render(request, 'taskcreate.html', {'pid':id})

def Detail(request, id):
	sel= Task.objects.get(id=id)
	return render(request, 'detail.html', {'data': sel})

def Taskupdate(request, id, tid):
	sel = Task.objects.get(id=tid)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=sel)
		form.save()
		return redirect('Taskdetail', id)
	else:
		form= Task.objects.get(id=tid)
	return render(request, 'taskcreate.html', {'data':form, 'pid':id})

def Taskdelete(request, id, tid):
	sel= Task.objects.get(id=tid)
	sel.delete()
	return redirect('Taskdetail', id)