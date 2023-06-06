from django.shortcuts import render, HttpResponse,redirect
import random  # import the random module
x=random.randint(1, 100)
print(x) 		# random number between 1-100 		# random number between 1-100
def index(request):
    return render(request, "index.html")
def result(request):
    numberfromform=request.POST['guessednumber']
    if ( x == int(numberfromform)):
        return render(request,("correct.html"))
    elif ( x > int(numberfromform)):
        return render(request,("toolow.html"))
    elif ( x < int(numberfromform)):
        return render(request,("toohigh.html"))
    else:
        return redirect('/')

