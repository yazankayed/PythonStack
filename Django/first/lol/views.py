from django.shortcuts import render, HttpResponse, redirect,jasonresponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f'placeholder to display the blog number {number}')
def edit(request, number):
    return HttpResponse(f'placeholder to edit blog {number}')
def destroy(request, number):
    return redirect('/blogs')
# Bonus question!
# def JsonMethod(request):
#     my_dict = {
#         "name": "yazan",
#         "age": 23,
#         "job": "Student"
#     }
#     return JsonResponse(my_dict, safe=False)


# def edit(request,number):
    
#     return HttpResponse("placeholder to display blog number: {number}")