from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='create'),
	path('show_booking/<int:booking_id>/', views.show_booking, name='show_booking'),
	path('bookings/', views.show_all_bookings, name='show_all_bookings'),
]