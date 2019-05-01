from django.urls import path
from . import views

urlpatterns = [
	path('', views.login),
	path('registration', views.registration, name='registration'),
	path('register', views.register, name='register'),
	path('homepage', views.homepage, name='homepage'),
	path('create', views.create, name='create'),
	path('delete', views.delete, name='delete'),
	path('update', views.update, name='update'),
]