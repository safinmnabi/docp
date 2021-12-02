from django.urls import path

from . import views

urlpatterns = [
	path('', views.Signin, name='Signin'),
	path('signup/', views.Signup, name='Signup'),
	path('signout/', views.Signout, name='Signout'),
	path('index/', views.Index, name='Index'),
	path('dataadd/', views.Datacreate, name='Datacreate'),
	path('update/<id>', views.Update, name='Update'),
	path('delete/<id>', views.Delete, name='Delete'),
	path('task/<id>', views.Taskdetail, name='Taskdetail'),
	path('addtask/<id>', views.Taskcreate, name='Taskcreate'),
	path('taskdetail/<id>', views.Detail, name='Detail'),
	path('taskupdate/<id>/<tid>', views.Taskupdate, name='Taskupdate'),
	path('taskdelete/<id>/<tid>', views.Taskdelete, name='Taskdelete'),
	# path('form/', views.form, name='form'),
	# path('detail/<id>', views.detail, name='detail'),
	# path('delete/<id>', views.delete, name='delete'),
	# path('update/<id>', views.update, name='update'),
	# # Login
	# path('lhome/', views.home, name='home'),
	# path('login/', views.login, name='login'),
	# path('logout/', views.logout, name='logout'),
	# path('signup/', views.signup, name='signup'),
]
