from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from content.models import *
from content.forms import IrisForm, UploadFileForm, UserFileForm
from django.conf import settings
import django.core.files.uploadedfile
from datetime import datetime
from django.contrib import messages
import os.path

#redirect to the login page
def login(request):
	return HttpResponseRedirect(reverse('login'))

#return the registration page
def registration(request):
	form = UserCreationForm()
	template_name = "registration/registration.html"
	return render(request, template_name, {'form': form})

#register the user
def register(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		user = form.save()
		return HttpResponse("<p>Registration success</p><a href=\"login\">Login</a>")
	else:
		errors = form.errors
		template_name = "registration/registration.html"
		return render(request, template_name, {'form': form, 'errors': errors})

def homepage(request, message=""):
	if request.user.is_superuser:
		role = "admin"
	else:
		role = "normal user"
	cat = 'files'
	table = "file list"
	form = UploadFileForm()
	entries = UserFile.objects.filter(owner=request.user)
	if 'cat' in request.POST:
		if request.POST['cat'] == "database":
			cat = "database"
			table = "Iris dataset"
			form = IrisForm()
			entries = Iris.objects.all()
	template_name = "homepage.html"
	return render(request, template_name, {'role': role, 'cat':cat, 'table': table, 'entries': entries, 'form': form})

#handle the create request
def create(request):
	data = request.POST.copy()
	sl = data.get('sepal_length')
	sw = data.get('sepal_width')
	pl = data.get('petal_length')
	pw = data.get('petal_width')
	c = data.get('CLASS')
	Iris.objects.create_iris(sl,sw,pl,pw,c).save()
	return HttpResponseRedirect(reverse('homepage'))

#handle the delete request
def delete(request):
	iris_id = request.POST.get('iris_id')
	Iris.objects.get(id=iris_id).delete()
	return HttpResponseRedirect(reverse('homepage'))

#handle the update request
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

def upload_file(request):
	if request.method == "POST":
		print("[debug] RECEIVED FORM", request.POST)
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			print("[debug] FORM VALID, file:", request.POST['title'])
			file = request.FILES['file']
			filename = request.POST['title']
			#handle_uploaded_file(filename, request.FILES['file'])
			f = UserFile.objects.create_file(filename, file.size, datetime.now(), request.user, request.FILES['file'])
			f.save()
			print(f)
			return HttpResponseRedirect(reverse('homepage'))
	return homepage(request)

def download_file(request):
	file_id = request.POST['file_id']
	file = UserFile.objects.get(id=file_id)
	if request.user != file.owner:
		return homepage(request, "You don't have access to the file!")
	else:
		path = os.path.join(settings.MEDIA_ROOT, 'userfile/'+file.filename)
		with open(path, 'rb') as f:
			response = HttpResponse(f.read(), content_type="multipart/form-data")
			response['Content-Disposition'] = 'attachment; filename="'+file.filename+'"'
			return response
"""
def handle_uploaded_file(name, f):
	with open(os.path.join(settings.MEDIA_ROOT+name), 'wb+') as destination:
		print("[debug] WRITE FILE TO:", settings.MEDIA_ROOT+'userfile/'+name)
		for chunk in f.chunks():
			destination.write(chunk)"""