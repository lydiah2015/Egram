from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Images,Profile, Comments
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def today_photos(request):
    images = Images.objects.all()
    return render(request, 'all-photos/photos.html', {"images": images,})

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

# def update_profile(request):
#     user = request.user
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_biography = form.cleaned_data['biography']
#             new_photo = form.cleaned_data['pic']
#             profile = Profile.objects.get(user=request.user)
#             profile.biography = new_biography
#             profile.profile_photo = new_photo
#             profile.save()
#             final_url = "/profile/" + str(request.user.id) + "/"
#             return redirect(final_url)
#     else:
#         form = ProfileForm()
#     return render(request, "update_profile.html", {"form": form})


