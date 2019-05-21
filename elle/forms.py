from django import forms
from .models import Image,Profile
from pyuploadcare.dj.forms import ImageField

class ImageForm(forms.ModelForm):
    image_url = ImageField(label='Picture')
    class Meta:
        model = Image
        fields = ("image","image_name","caption")

class ProfileForm(forms.Form):
    biography = forms.CharField(label = "Biography")
    profile_photos = ImageField(label = "profile_photos")
