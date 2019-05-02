from django import forms
from content.models import Iris, UserFile

class IrisForm(forms.ModelForm):
	class Meta:
		model = Iris
		fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'CLASS']

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=100)
	file = forms.FileField()
	
"""
class UserFileForm(forms.Form):
	class Meta:
		model = UserFile
		fields = ['filename', 'upload']
	
	title = forms.CharField(max_length=100)
	file = forms.FileField()
	def __init__(self,*args,**kwargs):
        self.site_id = kwargs.pop('site_id')
        super(StylesForm,self).__init__(*args,**kwargs)"""