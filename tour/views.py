from django.shortcuts import render, redirect
from .models import Tour
from review.models import Review
from .forms import TourForm
from django.db.models import Q


# Create your views here.
def index(request):
	tours = Tour.objects.all()
	return render(request, 'index.html', {
			'tours': tours
		})

def show_tour(request, tour_id):
	tour = Tour.objects.get(pk=tour_id)
	print(tour)
	reviews = Review.objects.filter(tour=tour)
	# reviews = Review.objects.get(tour=tour)
	print(reviews)
	return render(request, 'tour.html', {
			'tour': tour,
			'reviews': reviews
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

def add_tour(request):
	form = TourForm()
	if request.method == "POST":
		form = TourForm(request.POST, request.FILES)
		print(form)
		if form.is_valid:
			form.save()
			return redirect('tour:index')

	return render(request, 'add_tour.html', {
			'form': form
		})
