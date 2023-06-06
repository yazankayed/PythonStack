from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=245)
    age = models.IntegerField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



















# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)