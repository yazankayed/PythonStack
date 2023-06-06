from django.shortcuts import render,redirect
from . import models 
def index(request):
    models.show_all_dojo()
    # models.show_all_ninjas()
    context = {
        "dojos_names" : models.show_all_dojo(),
    }
    return render (request,'index.html',context)

def create_dojo(request):
    models.create_dojoo(request)
    return redirect('/')

def create_ninja(request):
    models.create_ninjoa(request)
    return redirect('/')