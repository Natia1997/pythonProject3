from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

    path('add_meal_to_room/<str:pk>/', views.add_meal_to_room, name='add_meal_to_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register')

]