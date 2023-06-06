from django.shortcuts import render, redirect, HttpResponse
from . import models

def index (request):
    context={
        'all_books': models.show_all_books()
    }
    return render(request,'index.html',context)

def book_details(request,num):
    context={
        'specific_book':models.Book.objects.get(id=num),
        'all_authors': models.show_all_authors(),
        'all_books': models.show_all_books()
    }
    return render (request,"book_details.html",context)


def add_book_to_author(request):
    models.add_book_to_Author(request)
    return redirect(request.META['HTTP_REFERER'])

def create_book(request):
    models.create_book(request)
    return redirect ('/')

def author(request):
    context={
        'all_authors': models.show_all_authors()
    }
    return render(request,'author_add.html',context)

def author_details(request,numb):
    context={
        'specific_author':models.Author.objects.get(id=numb),
        'all_authors': models.show_all_authors(),
        'all_books': models.show_all_books()
    }
    return render (request,"author_details.html",context)

def add_author_to_bok(request):
    models.add_author_to_book(request)
    return redirect(request.META['HTTP_REFERER'])




def create_author(request):
    models.create_author(request)
    return redirect ('/author')