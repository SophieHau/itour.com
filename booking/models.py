from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
	startdate = models.DateField(blank=True, null=True)
	enddate = models.DateField(blank=True, null=True)