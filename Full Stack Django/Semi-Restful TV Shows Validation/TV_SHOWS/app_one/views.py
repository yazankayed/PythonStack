from django.shortcuts import render,redirect ,HttpResponse
from . import models
from django.contrib import messages
from .models import Show


def index(request):
    return redirect('/shows/new')


def shows(request):
    return render(request,'index.html')

def createshow(request):
    
    errors = Show.objects.Show_validator(request.POST)
    if len(errors) > 0:  # if we have problems print the errors
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        models.showcreate(request)
        return redirect('shows/readone')          # if we do not have any problem with validation then insert data into DB

def test(request,num):
    
    context={
        'last_show':models.show_last_show(num)
    }
    
    return render(request,'readone.html',context)

def readone(request):
    context={
        'last_show':models.show_last_showw()
    }
    
    return render(request,'readone.html',context)


def readar(request):
    context={
        'all_shows': models.Show.objects.all
    }
    return render(request,'read.html',context)

def edit(request,num):
    context={
        'all_shows':models.show_all_shows().get(id=num)
    }
    return render(request,'edit_show.html',context)

def updateshow(request):
    x=request.POST['hidden_id']
    errors = Show.objects.Show_validator(request.POST)
    if len(errors) > 0:  # if we have problems print the errors
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{x}/edit')
    else:
        models.update_show(request)

        return redirect('/shows/readone')



    

def delete_show(request,num):
    models.delete_show(num)
    return redirect('/shows')
