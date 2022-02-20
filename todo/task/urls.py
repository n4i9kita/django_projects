# we connect urls to views. 
# call a view, when on a particular url
from django.urls import path
from . import views

# urlpatterns
urlpatterns=[
    path("", views.index),
]