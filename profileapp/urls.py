from django.urls import path, reverse, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('profileapp/', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('addprofile', views.addprofile, name='addprofile'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    # path('accounts/login', views.login, name='login'),
    #   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
