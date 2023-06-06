from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('lll', views.create_book ),
    path('author',views.author),
    path('authorcreation',views.create_author),
    path('books/<int:num>',views.book_details),
    path('authors/<int:numb>',views.author_details),
    path('addbtoa',views.add_book_to_author),
    path('addatob',views.add_author_to_bok),
]
