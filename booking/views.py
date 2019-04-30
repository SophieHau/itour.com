from django.shortcuts import render
from .forms import BookingForm

def create(request):
	form = BookingForm(request.POST)
	return render(request, 'booking.html', {
            'form': form,
       	})

