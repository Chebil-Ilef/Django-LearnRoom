from django.urls import path, include
from . import views

#Define the URL patterns for the app

urlpatterns = [
    path("", views.index, name="index"),
]