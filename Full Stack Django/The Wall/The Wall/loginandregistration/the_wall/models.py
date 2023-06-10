from django.db import models
from app_one.models import User

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , related_name="messages" , on_delete=models.DO_NOTHING)


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , related_name="comments" , on_delete=models.DO_NOTHING)
    message = models.ForeignKey(Message , related_name="comments" , on_delete=models.CASCADE)


def create_message(request):
    this_message = request.POST['post_message']
    this_user = User.objects.get(id = request.POST['catch_id'])
    Message.objects.create(message = this_message ,   user = this_user)


def show_msg():
    return Message.objects.all().order_by("-created_at")


def create_comment(request):
    this_user = User.objects.get(id = request.POST['comment_user_id'])
    this_msg = Message.objects.get(id = request.POST['comment_msg_id'])
    Comment.objects.create(comment = request.POST['write_comment'] , user = this_user , message =this_msg )

def delete_msg (request):
    delete_message= Message.objects.get(id = request.POST['delete_id'])
    delete_message.delete()