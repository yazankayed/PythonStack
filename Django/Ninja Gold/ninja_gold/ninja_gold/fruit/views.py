from django.shortcuts import render, redirect 
import random
from datetime import datetime
# Create your views here.
def index(request):
    if 'text' not in request.session:
        request.session['text'] = []

    if 'gold' not in request.session:
        request.session['gold'] = 0

    return render(request, 'index.html')

def location(request):
    winnings = 0
    if request.POST['location'] == 'farm':
        winnings = random.randint(10, 20) 

    elif request.POST['location'] == 'cave':
        winnings = random.randint(5, 10)

    elif request.POST['location'] == 'house':
        winnings = random.randint(2, 5)

    elif request.POST['location'] == 'casino':
        winnings = random.randint(-50, 50)

    request.session['gold'] += winnings

    local = request.POST['location']
    today = datetime.today()
    print(today)
    today.strftime("(%m/%d/%Y %I:%M:%S)")
    date_string = today.strftime("(%m/%d/%Y %I:%M:%S)")
    print("$" * 20)
    print(type(today))
    print(date_string)

    if winnings < 0:
        lose = f"Entered a {local} and lost {winnings} golds... Ouch..{date_string}"
        request.session['text'].append([lose, winnings])
    else:
        win = f"Earned {winnings} golds from the {local}!{date_string}"
        request.session['text'].append([win, winnings])
    
    return redirect('/')


def delete(request):
    request.session.clear()
    return redirect('/')
