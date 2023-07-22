from django.shortcuts import render
from . import proba

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Let\'s learn Python'},
    {'id': 2, 'name': 'Designing a Django app'},
    {'id': 3, 'name': 'Frontend development'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    szam = proba.hatvanyozas(int(pk))

    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break
    if room is not None:
        context = {'room': room}
        # egy próba
       # return render(request, 'base/room.html', {'number': szam})
        return render(request, 'base/room.html', context)

    return render(request, 'base/home.html')

# https://www.youtube.com/watch?v=PtQiiknWUcI 1:04:10