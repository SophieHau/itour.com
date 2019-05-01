from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='create'),
	path('create/<int:tour_id>', views.create, name='create'),
]