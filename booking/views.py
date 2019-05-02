from django.shortcuts import render, redirect
from . models import Booking
from tour.models import Tour
from .forms import BookingForm
from django.contrib.auth.models import User


def create(request, tour_id=None):
	if tour_id != None:
		tour = Tour.objects.get(pk=tour_id)
	else:
		tour = Tour.objects.first()
	form = BookingForm(initial={
			'tour': tour, 
			'price': tour.price, 
			'number_of_people': 1
		})
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			booking = form.save(False)
			if request.user.is_authenticated:
				booking.user = request.user
				booking.save()
			else:
				booking.save()
			return redirect('payment:make_payment', booking_id=booking.id)
	return render(request, 'booking.html', {
            'form': form,
       	})