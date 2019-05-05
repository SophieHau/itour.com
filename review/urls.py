from django.urls import path, reverse, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from review.views import requestAjax

from . import views

# app_name = 'review'

urlpatterns = [
	path('add_review', views.add_review, name='add_review'),
	path('ajax_sr/', requestAjax, name='ajax_sr'),
    # path('profile', views.profile, name='profile'),
    # path('addprofile', views.addprofile, name='addprofile'),
    # path('signin', views.signin, name='signin'),
    # path('signup', views.signup, name='signup'),
    # path('signout', views.signout, name='signout'),
]