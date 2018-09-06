from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^translate/', translate_view),
]