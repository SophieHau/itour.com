from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

	tour = models.ForeignKey()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    guestFirstName = models.CharField(max_length  = 255)
    guestLastName = models.CharField(max_length  = 255)
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    totalPrice = models.IntegerField(default = 0)
