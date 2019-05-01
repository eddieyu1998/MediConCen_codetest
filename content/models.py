from django.db import models

# Create your models here.
class IrisManager(models.Manager):
	def create_iris(self, sl, sw, pl, pw, c):
		iris = self.create(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw, CLASS=c)
		return iris

class Iris(models.Model):
	sepal_length = models.DecimalField(max_digits=2, decimal_places=1)
	sepal_width = models.DecimalField(max_digits=2, decimal_places=1)
	petal_length = models.DecimalField(max_digits=2, decimal_places=1)
	petal_width = models.DecimalField(max_digits=2, decimal_places=1)
	SETOSA = "SE"
	VERSICOLOUR = "VE"
	VIRGINICA = "VI"
	CLASS_CHOICES = (
		(SETOSA, "SETOSA"), 
		(VERSICOLOUR, "VERSICOLOUR"), 
		(VIRGINICA, "VIRGINICA")
	)
	CLASS = models.CharField(max_length=11, choices=CLASS_CHOICES)
	objects = IrisManager()