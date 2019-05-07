from django import forms
from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from .models import Payment



class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = ['first_name', 'last_name', 'email', 'method', 'card_name', 'card_number', 'card_date', 'card_cvv']
		labels = {
			'first_name': ('First Name'),
			'last_name': ('Last Name'),
			'email': ('Email'),
			'method': ('Method of Payment'),
			'card_name': ('Name on the card'),
			'card_number': ('Card Number'),
			'card_date': ('Expiration Date'),
			'card_cvv': ('CVV')
		}
		widgets = {
            'email': forms.EmailInput(),
        }