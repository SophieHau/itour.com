from django import forms
from django.forms import TextInput, NumberInput
from .models import Booking
from bootstrap_datepicker_plus import DatePickerInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tour', 'number_of_people', 'start_date', 'end_date', 'price']
        widgets = {
        # format='%d-%m-%Y'
            'start_date': DatePickerInput(attrs={'required':'required'}), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(attrs={'required':'required'}), # specify date-frmat
            'price': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control-plaintext'}),
            'number_of_people': forms.NumberInput(attrs={'min':1, 'max': 20}),
        }