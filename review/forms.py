from django import forms
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
from .models import Review
from tour.models import Tour


class ReviewForm(forms.ModelForm):
	tour = forms.ModelChoiceField(queryset=Tour.objects.all()) 
	rating = forms.ChoiceField(choices=Review.RATING_CHOICES, initial='good')
	text = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Review
		fields = ['tour', 'text', 'rating']
