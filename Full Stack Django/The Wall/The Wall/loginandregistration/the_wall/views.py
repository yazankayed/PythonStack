from django.shortcuts import render, redirect
from . import models


def wall(request):
    context = {
        "user": models.User.objects.get(id=request.session['userid']),
        "msg": models.show_msg
    }
    if request.session['userid']:
        return render(request, 'wall.html', context)
    else:
        return redirect('/')


def create_msg(request):
    models.create_message(request)
    return redirect('/wall')

def post_comment(request):
    models.create_comment(request)
    return redirect('/wall')

def delete_msg(request):
    models.delete_msg(request)
    return redirect('/wall')