from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Room


def add_room(request):

    if request.method == "POST":

        room_number = request.POST.get("room_number")
        room_type = request.POST.get("room_type")
        floor = request.POST.get("floor")
        total_beds = request.POST.get("total_beds")
        available_beds = request.POST.get("available_beds")
        rent = request.POST.get("rent")

        room_image = request.FILES.get("room_image")

        Room.objects.create(
            room_number=room_number,
            room_type=room_type,
            floor=floor,
            total_beds=total_beds,
            available_beds=available_beds,
            rent=rent,
            room_image=room_image
        )

        return redirect("view_rooms")

    return render(request,"add_room.html")



def view_rooms(request):

    rooms = Room.objects.all()

    return render(request,"view_rooms.html",{"rooms":rooms})



def delete_room(request,id):

    room = Room.objects.get(id=id)
    room.delete()

    return redirect("view_rooms")
  
from students.models import Student
from .models import Room

def assign_room(request):

    students = Student.objects.filter(room__isnull=True)
    rooms = Room.objects.filter(available_beds__gt=0)

    if request.method == "POST":

        student_id = request.POST.get("student")
        room_id = request.POST.get("room")

        student = Student.objects.get(id=student_id)
        room = Room.objects.get(id=room_id)

        if room.available_beds > 0:

            student.room = room
            student.save()

            room.available_beds -= 1
            room.save()

        return redirect("view_rooms")

    context = {
        "students":students,
        "rooms":rooms
    }

    return render(request,"assign_room.html",context)
  
def room_members(request,id):

    students = Student.objects.filter(room_id=id)

    return render(request,"room_members.html",{"students":students})
  
def vacate_room(request,id):

    student = Student.objects.get(id=id)

    room = student.room

    if room:

        room.available_beds += 1
        room.save()

        student.room = None
        student.save()

    return redirect("view_rooms")