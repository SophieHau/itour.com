from django.db import models
from booking.models import Booking


class Payment(models.Model):
	METHOD = (
        ('credit', 'Credit card'),
        ('debit', 'Debit card'),
        ('paypal', 'PayPal'),
    )

	booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=100, blank=False)
	method = models.CharField(max_length=20, choices=METHOD,
								default='credit')
	card_name = models.CharField(max_length=100, blank=False)
	card_number = models.IntegerField(blank=False)
	card_date = models.CharField(max_length=5, blank=False)
	card_cvv = models.IntegerField(blank=False)