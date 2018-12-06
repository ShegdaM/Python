from django.db import models
class Student(models.Model):
	name = models.CharField(max_length = 15)
	surname = models.CharField(max_length = 15)
	mark = models.CharField(max_length = 20)
	creator = models.CharField(max_length = 15,default='Anonymous')


class Profile(models.Model):
	name = models.CharField(max_length = 15)
	surname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15)
	location = models.CharField(max_length = 20)
	age = models.CharField(max_length = 2)
	img = models.CharField(max_length = 200)
