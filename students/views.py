from django.shortcuts import render, redirect
from .models import Student
from rooms.models import Room


def add_student(request):

    rooms = Room.objects.filter(available_beds__gt=0)

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        college = request.POST.get("college")
        course = request.POST.get("course")
        joining_date = request.POST.get("joining_date")

        room_id = request.POST.get("room")

        photo = request.FILES.get("photo")
        id_proof = request.FILES.get("id_proof")

        room = Room.objects.get(id=room_id)

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            college=college,
            course=course,
            joining_date=joining_date,
            room=room,
            photo=photo,
            id_proof=id_proof
        )

        room.available_beds -= 1
        room.save()

        return redirect("view_students")

    return render(request,"add_student.html",{"rooms":rooms})



def view_students(request):

    students = Student.objects.all()

    return render(request,"view_students.html",{"students":students})



def delete_student(request,id):

    student = Student.objects.get(id=id)

    room = student.room
    room.available_beds += 1
    room.save()

    student.delete()

    return redirect("view_students")
  
def student_register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        college = request.POST.get("college")
        course = request.POST.get("course")

        username = request.POST.get("username")
        password = request.POST.get("password")

        photo = request.FILES.get("photo")
        id_proof = request.FILES.get("id_proof")

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            college=college,
            course=course,
            username=username,
            password=password,
            photo=photo,
            id_proof=id_proof,
            joining_date=None
        )

        return redirect("student_login")

    return render(request,"student_register.html")
  
from django.contrib import messages
from fees.models import Fee
from complaints.models import Complaint


def student_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(
                username=username,
                password=password
            )

            request.session['student_id'] = student.id

            return redirect("student_dashboard")

        except:
            messages.error(request,"Invalid Credentials")

    return render(request,"student_login.html")
  
def student_dashboard(request):

    student_id = request.session.get('student_id')

    student = Student.objects.get(id=student_id)

    fees = Fee.objects.filter(student=student, status="Pending").count()

    complaints = Complaint.objects.filter(student=student).count()

    context = {
        "student":student,
        "fees":fees,
        "complaints":complaints
    }

    return render(request,"student_dashboard.html",context)
  
def student_logout(request):

    del request.session['student_id']

    return redirect("student_login")
  
def vacant_students(request):

    students = Student.objects.filter(room__isnull=True)

    return render(request,"vacant_students.html",{"students":students})


from notice.models import Notice  # import the Notice model

def student_notices(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    notices = Notice.objects.all().order_by('-date')  # latest first

    context = {
        "student": student,
        "notices": notices
    }
    return render(request, "student_notices.html", context)



def student_room(request):

    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)

    return render(request, "student_room.html", {"student": student})