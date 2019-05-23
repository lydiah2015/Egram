from django import forms
from .models import Images,Profile
from pyuploadcare.dj.forms import ImageField

class ImageForm(forms.ModelForm):
    image = ImageField(label='Picture')
    
    class Meta:
        model = Images
        fields = ("image_name","captions","image")

class ProfileForm(forms.Form):
    biography = forms.CharField(label = "Biography")
    profile_photos = ImageField(label = "profile_photos")
