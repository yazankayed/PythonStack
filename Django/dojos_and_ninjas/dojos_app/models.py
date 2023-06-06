from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc=models.CharField(max_length=255)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo,related_name="ninjas",on_delete = models.CASCADE)




def show_all_dojo():
    all_dojos=Dojo.objects.all()
    return all_dojos

def show_all_ninjas():
    all_ninjas=Ninja.objects.all()
    return all_ninjas
def create_dojoo(request):
    new_dojo = Dojo.objects.create(name = request.POST['dojo_name'] , city = request.POST['dojo_city'], state = request.POST['dojo_state'])
    return new_dojo
def create_ninjoa(request):
    new_ninja = Ninja.objects.create(first_name = request.POST['ninja_fname'] , last_name=request.POST['ninja_lname'],dojo=Dojo.objects.get(id=request.POST['dojos']))
    return new_ninja
