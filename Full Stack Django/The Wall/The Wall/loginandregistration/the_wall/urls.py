from django.urls import path
from . import views
urlpatterns = [
    path ('wall', views.wall) , 
    path ('message' , views.create_msg),
    path ('comment' , views.post_comment),
    path ('destroy' , views.delete_msg)
]
