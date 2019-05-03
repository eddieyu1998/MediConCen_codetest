from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from content.models import *
from content.forms import IrisForm, UploadFileForm
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

def homepage(request, message="", update=""):
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
	if update:
		update = int(update)
	template_name = "homepage.html"
	return render(request, template_name, {'role': role, 'cat':cat, 'table': table, 
		'entries': entries, 'form': form, 'message': message, 'update': update})

#deprecated
def create(request):
	data = request.POST.copy()
	sl = data.get('sepal_length')
	sw = data.get('sepal_width')
	pl = data.get('petal_length')
	pw = data.get('petal_width')
	c = data.get('CLASS')
	Iris.objects.create_iris(sl,sw,pl,pw,c).save()
	return HttpResponseRedirect(reverse('homepage'))

#deprecated
def delete(request):
	iris_id = request.POST.get('iris_id')
	Iris.objects.get(id=iris_id).delete()
	return HttpResponseRedirect(reverse('homepage'))

#deprecated
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

#used for generating hash id for files
def sdbm_hash(instr):
	hash = 0
	for c in instr:
		hash = int(ord(c)) + (hash << 6) + (hash << 16) - hash
	return hash & 0x7fffffffffffffff

#for user to upload files
def upload_file(request):
	if request.method == "POST":
		file = request.FILES['file']
		split = file.name.split('.')
		if len(split) > 2:
			filename = ".".join(split[0:-1])
			filetype = "."+split[-1]
		elif split[0] == "" or len(split) == 1:
			filename = file.name
			filetype = ""
		else:
			filename = split[0]
			filetype = "."+split[-1]
		filesize = file.size
		hash_id = sdbm_hash(str(request.user.id)+str(request.user)+filename+str(filesize)+str(datetime.now()))
		f = UserFile.objects.create_file(hash_id, filename, filetype, filesize, datetime.now(), request.user)
		f.upload = file
		f.save()
		return HttpResponseRedirect(reverse('homepage'))
	return homepage(request)

#for user to download files
def download_file(request):
	file_id = request.POST['file_id']
	file = UserFile.objects.get(hash_id=int(file_id))
	if request.user != file.owner:
		return homepage(request, "You don't have access to the file!")
	else:
		response = HttpResponse(file.upload, content_type="multipart/form-data")
		response['Content-Disposition'] = 'attachment; filename="'+file.filename+file.filetype+'"'
		return response

#for user to delete files
def delete_file(request):
	if request.method == "POST":
		file_id = request.POST['file_id']
		file = UserFile.objects.get(hash_id=int(file_id))
		if request.user != file.owner:
			return homepage(request, "You don't have access to the file!")
		else:
			file.upload.delete()
			file.delete()
			return HttpResponseRedirect(reverse('homepage'))
	return homepage(request)

#get the entry user want to update, and update the view accordingly
def update_file(request):
	file_id = request.POST['file_id']
	return homepage(request, update=file_id)

#apply the update
def handle_update_file(request):
	if request.method == "POST":
		file_id = request.POST['file_id']
		file = UserFile.objects.get(hash_id=file_id)
		if request.user != file.owner:
			return homepage(request, "You don't have access to the file!")
		else:
			filename = request.POST['filename']
			file.filename = filename
			file.last_modified = datetime.now()
			file.save()
			if request.FILES:
				file.upload.delete()
				split = request.FILES['file'].name.split('.')
				if len(split)>2:
					file.filetype = "."+split[-1]
				elif split[0] == "" or len(split) == 1:
					file.filetype = ""
				else:
					file.filetype = "."+split[-1]
				file.filesize = request.FILES['file'].size
				file.upload = request.FILES['file']
				file.save()
			return HttpResponseRedirect(reverse('homepage'))
	return homepage(request)