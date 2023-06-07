from django.shortcuts import render,redirect ,HttpResponse
from . import models


def index(request):
    return redirect('/shows/new')


def shows(request):
    return render(request,'index.html')

def createshow(request):
    models.showcreate(request)
    return redirect('shows/readone')

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
    models.update_show(request)
    
    return redirect('/shows/readone')

def delete_show(request,num):
    models.delete_show(num)
    return redirect('/shows')
