from django.db import models

# Create your models here.
class Image:
    image=models.ImageField
    image_name=models.CharField(max_length=15)
    image_caption=models.CharField(max_length=30)
    comments=models.CharField(max_length=50)
    likes=models

class Profile:
    profile_photo=models.ImageField
    biography=models.CharField(max_length=30)


