from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#Manager for creating instance of Iris
class IrisManager(models.Manager):
	def create_iris(self, sl, sw, pl, pw, c):
		iris = self.create(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw, CLASS=c)
		return iris

class Iris(models.Model):
	sepal_length = models.DecimalField(max_digits=2, decimal_places=1)
	sepal_width = models.DecimalField(max_digits=2, decimal_places=1)
	petal_length = models.DecimalField(max_digits=2, decimal_places=1)
	petal_width = models.DecimalField(max_digits=2, decimal_places=1)
	SETOSA = "SETOSA"
	VERSICOLOUR = "VERSICOLOUR"
	VIRGINICA = "VIRGINICA"
	CLASS_CHOICES = (
		(SETOSA, "SETOSA"), 
		(VERSICOLOUR, "VERSICOLOUR"), 
		(VIRGINICA, "VIRGINICA")
	)
	CLASS = models.CharField(max_length=11, choices=CLASS_CHOICES)
	objects = IrisManager()

class UserFileManager(models.Manager):
	def create_file(self, fn, fs, lm, o, u):
		f = self.create(filename=fn, filesize=fs, last_modified=lm, owner=o, upload=u)
		return f

class UserFile(models.Model):
	filename = models.CharField(max_length=100)
	filesize = models.IntegerField()
	last_modified = models.DateTimeField(default=datetime.now())
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	upload = models.FileField(upload_to='userfile')
	objects = UserFileManager()