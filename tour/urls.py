from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
	path('', views.index, name='index'),
	path('tours/tour/<int:tour_id>', views.show_tour, name='show_tour'),
	path('tours/search', views.search_tours, name='search_tours'),
	path('tours/', views.show_all_tours, name='show_all_tours'),
	path('tours/add', views.add_tour, name='add_tour'),
	path('tours/edit/<int:tour_id>', views.edit_tour, name='edit_tour'),
	path('tours/delete/<int:tour_id>', views.delete_tour, name='delete_tour'),
	path('contact/', views.send_message, name='send_message'),
]