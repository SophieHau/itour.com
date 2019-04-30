from django.shortcuts import render, redirect
from . models import Booking
from .forms import BookingForm
from django.contrib.auth.models import User



def create(request):
	form = BookingForm()
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			booking = form.save(False)
			print(form)
			booking.user = request.user
			booking.save()
			return redirect('tour:index')
	return render(request, 'booking.html', {
            'form': form,
       	})