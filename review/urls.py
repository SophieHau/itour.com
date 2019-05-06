from django.urls import path, reverse, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from . import views

# app_name = 'review'

urlpatterns = [
	path('add_review', views.add_review, name='add_review'),
]