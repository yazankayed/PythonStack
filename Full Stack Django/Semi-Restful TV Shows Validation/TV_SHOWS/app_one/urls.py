from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('shows/new', views.shows),
    path('shows', views.readar),
    path('pcreate',views.createshow),
    path('shows/readone', views.readone),	
    path('shows/<int:num>/edit', views.edit),
    path('shows/pupdate',views.updateshow),
    path('shows/<int:num>', views.test),
    path('deleteshow/<int:num>', views.delete_show),
]
