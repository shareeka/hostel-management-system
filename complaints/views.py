from django.shortcuts import render, redirect
from .models import Complaint
from students.models import Student


from django.shortcuts import render, redirect
from .models import Complaint
from students.models import Student
from django.contrib import messages

# Add complaint (student side)
def add_complaint(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        Complaint.objects.create(
            student=student,
            title=title,
            description=description
        )
        messages.success(request, "Complaint submitted successfully")
        return redirect("student_dashboard")

    return render(request, "add_complaint.html", {"student": student})



def view_complaints(request):

    complaints = Complaint.objects.all()

    return render(request,"view_complaints.html",{"complaints":complaints})



def resolve_complaint(request,id):

    complaint = Complaint.objects.get(id=id)

    complaint.status = "Resolved"
    complaint.save()

    return redirect("view_complaints")