from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter']+=1
    dicct={
        "counter":request.session['counter']
    }
    return render(request,"index.html",dicct)

def clearsessionn(request):
    if 'counter' in request.session:
        del request.session['counter']
    return redirect("/")
    