from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
	path('payment/<int:booking_id>', views.make_payment, name='make_payment'),
]