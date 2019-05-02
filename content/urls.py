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
	path('upload_file', views.upload_file, name='upload_file'),
	path('download_file', views.download_file, name='download_file'),
	path('delete_file', views.delete_file, name='delete_file')
]