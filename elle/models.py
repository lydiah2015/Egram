from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'gramm/')
    biography = models.CharField(max_length= 50)


class Images(models.Model):
    image = models.ImageField(upload_to = 'gramm/')
    image_name = models.CharField(max_length=15)
    image_caption = models.CharField(max_length=30)
    # comments = models.CharField(max_length=50)
    # likes=models.IntegerField()
    profile_photo=models.ForeignKey(Profile)
   

class Comments(models.Model):
    profile_photo=models.ForeignKey(Profile)
    


