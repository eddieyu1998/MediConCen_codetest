from django.forms import ModelForm
from content.models import Iris

class IrisForm(ModelForm):
	class Meta:
		model = Iris
		fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'CLASS']