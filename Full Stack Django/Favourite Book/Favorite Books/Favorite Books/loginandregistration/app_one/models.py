from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        x = User.objects.filter(email=postData['email'])    
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password description should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Password conformation didn't match"
        if  len(x)>0:
            errors['emaill'] = "Email Already Used!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}


        if len(postData['book_title']) < 1:
            errors["title"] = "Book Title is required"
        if len(postData['book_desc']) < 3:
            errors["desc"] = "Book Description is required"


        return errors



class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploded_by = models.ForeignKey(User, related_name="books", on_delete = models.CASCADE)
    users_who_like= models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()


def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['fname'] ,last_name = request.POST['lname'] , email = request.POST['email'] , 
                        password= pw_hash )
    

# def login(request):
#     user = User.objects.get(email = request.POST['email'])
#     if user :
#         logged_user = user.email
    
#     if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
#         request.session['userid'] = logged_user.id


def create_a_book(request):
    return Book.objects.create(title=request.POST['book_title'],description=request.POST['book_desc'],uploded_by=User.objects.get(id =request.session['userid']))


def specific_book(useridd):
    return Book.objects.get(id=useridd)

def update_abook(request):
    book_to_update=Book.objects.get(id=request.POST['hiiden_id'])
    book_to_update.description=request.POST['updated_textarea']
    book_to_update.save()
    return book_to_update


def add_to_favr(request,bookiid):
    this_book = Book.objects.get(id=bookiid)
    user = User.objects.get(id=request.session['userid'])
    user.liked_books.add(this_book)

def remove_from_favr(request,bookiid):
    this_book = Book.objects.get(id=bookiid)
    user = User.objects.get(id=request.session['userid'])
    user.liked_books.remove(this_book)