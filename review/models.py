from django.db import models
from django.contrib.auth.models import User
from booking.models import Booking
from tour.models import Tour

# Create your models here.
class Review(models.Model):
	RATING_CHOICES = (
    ("poor", "poor"),
    ("fair", "fair"),
    ("good", "good"),
    ("very good", "very good"),
    ("excelent", "excelent"),
)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=1, related_name='review_booking')
	text = models.CharField(default='', blank=True, null=True, max_length = 100)
	rating = models.CharField(choices=RATING_CHOICES, default="good", max_length=9)
	date = models.DateTimeField(auto_now_add=True)	
	def __str__(self):
		return self.user.username + ' - ' + str(self.date)