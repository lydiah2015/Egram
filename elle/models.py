from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'image/')
    biography = models.CharField(max_length= 50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Images(models.Model):
    image = models.ImageField(upload_to = 'gramm/')
    image_name = models.CharField(max_length=15)
    captions = models.CharField(max_length=50)
    # likes=models.IntegerField(User, related_name = "likes", blank = True)
    profile_photo=models.ForeignKey(Profile)
    user = models.ForeignKey(User, related_name = "posts", blank = True)
   
def save_image(self):
    self.save()

def delete_image(self):
    cls.objects.get(id = self.id).delete()

def update_caption(self,new_caption):
    self.caption = new_caption
    self.save()


class Comments(models.Model):
    image = models.ForeignKey(Images,related_name = "comments")
    comm = models.CharField(max_length = 100, blank = True)
    user = models.ForeignKey(User, related_name = "comments")

def save_comment(self):
    self.save()

def delete_comment(self):
    Comments.objects.get(id = self.id).delete()
    
def update_comment(self,new_comment):
    comm = Comments.objects.get(id = self.id)
    comm.comment = new_comment
    comm.save()



