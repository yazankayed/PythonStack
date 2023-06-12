from django.shortcuts import render, redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import User
from .models import Book
import bcrypt




def add_to_favorites(request,bookiid):
    models.add_to_favr(request,bookiid)
    return redirect('/books')


def unadd_to_favorites(request,bookiidd):
    models.remove_from_favr(request,bookiidd)
    return redirect('/books')




def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        models.register(request)
        
        return redirect('/')



def success(request):
    if  'userid' not in request.session:
        return redirect('/')
    else:
        context = {
                "display_all_books": models.Book.objects.all(), 
                "logged_user" : models.User.objects.get(id=request.session['userid'])
            }
        return render(request,'welcome.html' , context)


def create_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        models.create_a_book(request)
        x=models.Book.objects.last()
        models.add_to_favr(request,x.id)
        return redirect('/books')


def book_details(request,useridd):
    context={
        'getting_specific_book': models.specific_book(useridd),
        "logged_user" : models.User.objects.get(id=request.session['userid']),
        # "user_id" : request.session['userid']
    }
    return render(request,'book_deatils.html',context)


def book_update(request):
    models.update_abook(request)
    x= request.POST['hiiden_id']
    return redirect(f'/books/{x}')



def login(request):
    user = User.objects.filter(email = request.POST['person_email'])
    if not user:
        return redirect('/')
    else :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/books')
    


def logout(request):
    del request.session['userid']
    return redirect('/')
