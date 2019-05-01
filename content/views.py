from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from content.models import *
from content.forms import IrisForm
# Create your views here.
def login(request):
	return HttpResponseRedirect(reverse('login'))

def registration(request):
	form = UserCreationForm()
	template_name = "registration/registration.html"
	return render(request, template_name, {'form': form})

def register(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		user = form.save()
		return HttpResponse("<p>Registration success</p><a href=\"login\">Login</a>")
	else:
		errors = form.errors
		template_name = "registration/registration.html"
		return render(request, template_name, {'form': form, 'errors': errors})

def homepage(request):
	if request.user.is_superuser:
		role = "admin"
	else:
		role = "normal user"
	table = "Iris dataset"
	iris_list = Iris.objects.all()
	form = IrisForm()
	template_name = "homepage.html"
	return render(request, template_name, {'role': role, 'table': table, 'iris_list': iris_list, 'form': form})

def create(request):
	data = request.POST.copy()
	sl = data.get('sepal_length')
	sw = data.get('sepal_width')
	pl = data.get('petal_length')
	pw = data.get('petal_width')
	c = data.get('CLASS')
	Iris.objects.create_iris(sl,sw,pl,pw,c).save()
	return HttpResponseRedirect(reverse('homepage'))

def delete(request):
	iris_id = request.POST.get('iris_id')
	Iris.objects.get(id=iris_id).delete()
	return HttpResponseRedirect(reverse('homepage'))

def update(request):
	data = request.POST.copy()
	iris_id = request.POST.get('iris_id')
	sl = data.get('sepal_length')
	sw = data.get('sepal_width')
	pl = data.get('petal_length')
	pw = data.get('petal_width')
	c = data.get('CLASS')
	Iris.objects.filter(id=iris_id).update(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw)
	return HttpResponseRedirect(reverse('homepage'))