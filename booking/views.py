from django.shortcuts import render, redirect
from . models import Booking
from tour.models import Tour
from .forms import BookingForm
from django.contrib.auth.models import User
import json


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
    
    tour_data = to_json(get_tours_data())
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(False)
            tour = booking.tour
            booking.price = booking.number_of_people * tour.price 
            if request.user.is_authenticated:
                booking.user = request.user
                booking.save()
            else:
                booking.save()
            return redirect('payment:make_payment', booking_id=booking.id)
    return render(request, 'booking.html', {
            'form': form,
            'tour_data': tour_data,
        })


def show_booking(request, booking_id):
	booking = Booking.objects.get(pk=booking_id)
	return render(request, 'my_booking.html', {
		'booking': booking
		})


def show_all_bookings(request):
	bookings = Booking.objects.all()
	return render(request, 'bookings.html', {
		'bookings': bookings
		})

def get_tours_data():
    tours = Tour.objects.all()
    tour_dict = {}
    for tour in tours:
        tour_dict[tour.pk] = str(tour.price)
    return tour_dict 


def to_json(data):
    json_data = json.dumps(data)
    return json_data
