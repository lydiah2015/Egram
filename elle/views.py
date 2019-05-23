from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Images,Profile, Comments, Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def today_photos(request):
    images = Images.objects.all()
    return render(request, 'all-photos/photos.html', {"images": images})

def my_profile(request):
    user = request.user
    return render(request, "my_profile.html", {"user": user, "current_user": request.user})  

def add_image(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = user
            image.save()
            return redirect("today_photos")
    else:
        form = ImageForm()
    return render(request, "add_image.html", {"form": form})

def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_biography = form.cleaned_data['biography']
            new_photo = form.cleaned_data['profile_photos'] 
            profile = Profile.objects.get(user=request.user)
            profile.biography = new_biography
            profile.profile_photos = new_photo
            profile.save()
            final_url = "/profile/" + str(request.user.id) + "/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form": form})

def profile(request, id):
    user = User.objects.get(id=id)
    followers = user.user_followers.all()
    followers_arr = []
    for follower in followers:
        followers_arr.append(follower.followed_by.id)

    if request.user.id in followers_arr:
        is_following = True
    else:
        is_following = False

    if request.user.id == int(id):
        return redirect("my_profile")
    else:
        return render(request, "profile.html", {"user": user, "current_user": request.user, "is_following": is_following})

