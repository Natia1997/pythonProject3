from django.shortcuts import render
from . models import Room
from django.shortcuts import render, redirect, HttpResponse
from .form import MealForm


def home (request):
    ro=Room.objects.all()
    context={'ro': ro}
    return render (request, 'base/home.html', context)


def room(request, pk):

    room = Room.objects.get(id=int(pk))
    context = {'room': room}
    return render(request, 'base/rooms.html', context)




def add_meal_to_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.room = room
            meal.save()

            return redirect('room', pk=room.id)

    else:
        form = MealForm()

    return render(request, 'base/add_meal_to_room.html', {'room': room, 'form': form})


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'obj': room}
    if request.method == "POST":

        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)
