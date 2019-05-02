from django.db import models
from django.contrib.auth.models import User
from tour.models import Tour


class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
	number_of_people = models.IntegerField()
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

	def __str__(self):
		return self.user.username + ' - ' + str(self.start_date)