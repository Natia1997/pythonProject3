from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

    path('add_meal_to_room/<str:pk>/', views.add_meal_to_room, name='add_meal_to_room')

]