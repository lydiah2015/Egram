from django.shortcuts import render
from django.http import HttpResponse
from .models import Images
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def today_photos(request):
    images = Images.objects.all()

    return render(request, 'all-photos/photos.html', {"images": images,})

    