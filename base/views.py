from django.shortcuts import render
from .models import Room

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Let\'s learn Python'},
    {'id': 2, 'name': 'Designing a Django app'},
    {'id': 3, 'name': 'Frontend development'},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
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

