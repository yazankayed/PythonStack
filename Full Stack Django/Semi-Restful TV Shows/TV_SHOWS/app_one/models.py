from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def showcreate(request):
    Show.objects.create(title=request.POST['show_title'],network=request.POST['show_network'],release_date=request.POST['releasedate'],description=request.POST['show_desc'])

def show_last_show(id):
    return Show.objects.get(id=id)
def show_last_showw():
    return Show.objects.last

def show_all_shows():
    return Show.objects.all()
def update_show(request):
    show_to_update=Show.objects.get(id=request.POST['hidden_id'])
    show_to_update.title=request.POST['show_title']
    show_to_update.network=request.POST['show_network']
    
    show_to_update.description=request.POST['show_desc']
    show_to_update.save()
def delete_show(num):
    show_to_delete=Show.objects.get(id=num)
    show_to_delete.delete()
    
