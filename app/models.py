from django.db import models

class User(models.Model):
	email = models.CharField(max_length=60)
	password = models.CharField(max_length=150)

	def __str__(self):
		return self.username
		
class Person(models.Model):
	name = models.CharField(max_length=60)
	job = models.CharField(max_length=60)
	mobile = models.CharField(max_length=30)
	eid = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Task(models.Model):
	taskname = models.CharField(max_length=30)
	detail = models.CharField(max_length=50)
	pid = models.CharField(max_length=50)

	def __str__(self):
		return self.taskname