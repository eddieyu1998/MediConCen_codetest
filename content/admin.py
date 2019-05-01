from django.contrib import admin
from .models import *
from django.apps import apps

# Register your models here.
models = apps.get_app_config('content')

for name, model in models.models.items():
    admin.site.register(model)