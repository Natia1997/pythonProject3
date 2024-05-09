from django.shortcuts import render
from . models import Room

#ro=[{'id': 1, "name": "30 Minutes or less"}, {'id': 2, "name": "5 Ingredients or less"},{'id': 3, "name": "kid approved"}, {'id': 4, "name": "Special diets"}, {'id': 5, "name": "Cook for one or two"}, {'id': 6, "name": "Cooking for a crowd"},{'id': 7, "name": "Vegan brother-in-law"}]


def home (request):
    ro=Room.objects.all()
    context={'ro': ro}
    return render (request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=int(pk))
    context = {'room': room}
    return render(request, 'base/rooms.html',context)
