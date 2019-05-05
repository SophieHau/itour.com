from django import forms
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
from .models import Review
from booking.models import Booking
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['booking'] = forms.ModelChoiceField(
            queryset=Booking.objects.filter(user=user))
		
	# booking = forms.ModelChoiceField(queryset=Booking.objects.all())
	rating = forms.ChoiceField(choices=Review.RATING_CHOICES, initial='good')
	text = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Review
		fields = ['booking', 'text', 'rating']
