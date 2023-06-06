from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    desc = models.TextField(default="No Comment")


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="Nothing")
    books = models.ManyToManyField(Book , related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


def show_all_authors():
    return Author.objects.all()

def show_all_books():
    return Book.objects.all()

def add_book_to_Author(request):
    this_book = Book.objects.get(id=int(request.POST['btoa']))
    this_publisher = Author.objects.get(id=int(request.POST['book_to_author']))
    this_publisher.books.add(this_book)

def add_author_to_book(request):
    this_book = Book.objects.get(id=int(request.POST['author_to_book']))
    this_publisher = Author.objects.get(id=int(request.POST['atob']))
    this_book.authors.add(this_publisher)


def create_book(request):
    new_book= Book.objects.create(title=request.POST['book_title'],desc=request.POST['description_book'])
    return new_book

def create_author(request):
	new_author = Author.objects.create(first_name=request.POST['author_first_name'],last_name=request.POST['author_last_name'],notes=request.POST['author_notes'])
	return new_author

