from django.shortcuts import render, redirect
from .models import Tour
from review.models import Review
from booking.models import Booking
from .forms import TourForm
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


def index(request):
    tours = Tour.objects.all()
    return render(request, 'index.html', {
            'tours': tours
        })

def show_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    bookings = Booking.objects.filter(tour=tour)
    print(bookings)
    # reviews = bookings.review_set.all()
    # reviews = Review.objects.filter(booking=bookings)
	# reviews = Review.objects.get(tour=tour)
    print(bookings)
    return render(request, 'tour.html', {'tour': tour,
			'bookings': bookings
		})


def show_all_tours(request):
    tours = Tour.objects.all()
    return render(request, 'tours_list.html', {
            'tours': tours
        })


def search_tours(request):
    context = None
    if request.method != 'POST':
        return redirect('index')

    text = request.POST.get('search', '')
    results = Tour.objects.filter(
        Q(name__icontains=text) |
        Q(description__icontains=text) |
        Q(location__icontains=text) |
        Q(company__icontains=text)
        )
    return render(request, 'search_results.html', {
            'results': results,
            'text': text,
        })

@permission_required('tour.add_tour', login_url='signin')
def add_tour(request):
    form = TourForm()
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('tour:index')

    return render(request, 'add_tour.html', {
            'form': form
        })

@permission_required('tour.edit_tour', login_url='signin')
def edit_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    form = TourForm(instance=tour)
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid:
            form.save()
            return redirect('tour:index')

    return render(request, 'edit_tour.html', {
            'form': form,
            'tour': tour
        })

@permission_required('tour.delete_tour', login_url='signin')
def delete_tour(request, tour_id):
    tour = Tour.objects.filter(pk=tour_id).delete()
    return redirect('tour:index')

def send_message(request):
    if request.method=="POST":
        email = request.POST['email']
        message = request.POST['message']
        send_mail('message', message, email, ['support@itour.com'], fail_silently=False)
        
        return render(request, 'message_sent_confirmation.html', {
                'email': email,
            })
