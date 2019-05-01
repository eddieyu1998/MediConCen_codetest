from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
	template_name = "homepage.html"
	return render(request, template_name, {'role': role})