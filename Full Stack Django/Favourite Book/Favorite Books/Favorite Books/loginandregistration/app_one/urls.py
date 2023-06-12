from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),	
    path('books', views.success),
    path('books/<int:useridd>', views.book_details),
    path('update', views.book_update),	
    path('login', views.login),	
    path('logout', views.logout),
    path('createbook', views.create_book),		
    path('add/<int:bookiid>', views.add_to_favorites),
    path('unadd/<int:bookiidd>', views.unadd_to_favorites),		
]
