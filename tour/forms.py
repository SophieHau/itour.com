from django.forms import ModelForm
from .models import Tour

class TourForm(ModelForm):
	class Meta:
		model = Tour
		fields = '__all__'