from django.shortcuts import render, redirect
from . models import Booking
from review.models import Review
from tour.models import Tour
from .forms import BookingForm
from django.contrib.auth.models import User
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from datetime import datetime

def create(request, tour_id=None):
    if tour_id != None:
        tour = Tour.objects.get(pk=tour_id)
    else:
        tour = Tour.objects.first()
    form = BookingForm(initial={
         
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


def fetch_reviews(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    # bookings = Booking.objects.filter(tour=tour)
    # print(bookings)
    # # data = {
    #     'bookings': Booking.objects.filter(tour=tour)
    # }
    # bookings = Booking.objects.filter(tour=tour).values()
    bookings = Booking.objects.filter(tour=tour)
    print('bookings')
    print(bookings)
    review = ''
    for booking in bookings:
        review = booking.review_booking.all()
    print('review')
    print(review)
    if review.count() > 0:
        rating = review[0].rating
        user = review[0].user.username
        date = review[0].date
    else:
        rating = 'good'
        user = 'anonymous'
        date = str(datetime.now())
    json = {}
    json['rating'] = rating
    json['user'] = user
    json['date'] = date
    print('json')
    print(json)
    return JsonResponse(json, safe=False)
   