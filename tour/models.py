from django.db import models


class Tour(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	location = models.CharField(max_length=150)
	length = models.IntegerField()
	pic = models.ImageField(upload_to='images')
	company = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	def __str__(self):
		return self.name