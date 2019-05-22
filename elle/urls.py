from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
     url('^$',views.today_photos,name='today_photos'),
     url(r"^add/image/$", views.add_image, name = "add_image"),
     url(r"^accounts/profile/$", views.my_profile, name = "my_profile"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)