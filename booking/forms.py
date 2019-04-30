from django import forms
from django.forms import TextInput
from .models import Booking
from bootstrap_datepicker_plus import DatePickerInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['startdate', 'enddate']
        widgets = {
        # format='%d-%m-%Y'
            'startdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'enddate': DatePickerInput(), # specify date-frmat
        }