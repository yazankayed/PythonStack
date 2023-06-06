from django.shortcuts import render, HttpResponse, redirect
from . models import Users
def index(request):
    context = {
        "users_information": Users.objects.all()
    }
    return render(request,"index.html", context)

def add_user(request):
    first_name = request.POST['first_name']
    last_name =  request.POST['last_name']
    email_address =  request.POST['email']
    age =  request.POST['age']
    new_user = Users.objects.create(first_name=first_name,last_name=last_name,email_address=email_address,age=age) 
    return redirect('/')