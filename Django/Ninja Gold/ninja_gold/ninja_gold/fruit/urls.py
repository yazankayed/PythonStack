from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('location', views.location),
    path('delete', views.delete),
]