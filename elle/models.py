from django.db import models

# Create your models here.
class Image:
    image=models.ImageField(upload_to = 'today-photos.html/')
    image_name=models.CharField(max_length=15)
    image_caption=models.CharField(max_length=30)
    comments=models.CharField(max_length=50)
    # likes=models
    profile_photo=models.ForeignKey(Profile)

    
class Profile:
    profile_photo=models.ImageField(upload_to = 'today-photos.html/')
    biography=models.CharField(max_length=30)


