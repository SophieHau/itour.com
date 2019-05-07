from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
	path('payment', views.make_payment, name='make_payment'),
]