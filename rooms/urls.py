from django.urls import path
from . import views

urlpatterns = [

path('add-room/', views.add_room, name="add_room"),
path('view-rooms/', views.view_rooms, name="view_rooms"),
path('delete-room/<int:id>/', views.delete_room, name="delete_room"),

path('assign-room/', views.assign_room, name="assign_room"),
path('room-members/<int:id>/', views.room_members, name="room_members"),
path('vacate-room/<int:id>/', views.vacate_room),
]