from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Profile
from django.core.files.storage import FileSystemStorage


def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            if request.FILES['profile_pic']:
              profile_pic = request.FILES['profile_pic']
              fs = FileSystemStorage(location='media/images', base_url='/media/images')
              filename = fs.save(profile_pic.name, profile_pic)
              uploaded_file_url = fs.url(filename)
              profile.pic = uploaded_file_url
              profile.save()
        return render(request, 'profile.html', {'profile': profile})
    else:
        return render(request, 'signin.html')



def add_bio(request):
  if request.user.is_authenticated:
      user = request.user
      profile = Profile.objects.get(user_id=user.id)
      if request.method == 'POST':
        profile_bio = request.POST['bio']
        profile.bio = profile_bio
        profile.save()        
        return redirect('profile')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tour:index')
        else:
            # flash('This is error message', 'error')
            messages.add_message(request, messages.ERROR, 'Wrong user or password')
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            user.save()
            profile = Profile(user_id=user.id)
            profile.save()
            login(request, user)
            return redirect('tour:index')
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return render(request, 'signin.html')
