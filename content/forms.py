from django import forms
from content.models import Iris, UserFile

class IrisForm(forms.ModelForm):
	class Meta:
		model = Iris
		fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'CLASS']

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=100)
	file = forms.FileField()
