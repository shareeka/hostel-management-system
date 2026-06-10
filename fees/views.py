from django.shortcuts import render, redirect
from .models import Fee
from students.models import Student


def add_fee(request):

    students = Student.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student")
        month = request.POST.get("month")
        amount = request.POST.get("amount")

        student = Student.objects.get(id=student_id)

        Fee.objects.create(
            student=student,
            month=month,
            amount=amount,
            status="Pending"
        )

        return redirect("view_fees")

    return render(request,"add_fee.html",{"students":students})


def view_fees(request):

    fees = Fee.objects.all()

    return render(request,"view_fees.html",{"fees":fees})



def mark_paid(request,id):

    fee = Fee.objects.get(id=id)
    fee.status = "Paid"
    fee.save()

    return redirect("view_fees")
  
from students.models import Student
from .models import Fee

from django.shortcuts import render
from .models import Student
from fees.models import Fee

def student_fees(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return render(request, 'student_error.html', {'message': 'You must log in first to access this page.'})

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return render(request, 'student_error.html', {'message': 'Student not found. Please login again.'})

    fees = Fee.objects.filter(student=student)
    return render(request, 'student_fees.html', {'fees': fees})


from django.shortcuts import redirect
from .models import Fee
from django.shortcuts import redirect
from .models import Fee
from django.utils import timezone


def pay_fee(request,id):

    fee = Fee.objects.get(id=id)

    fee.status = "Paid"
    fee.payment_date = timezone.now()   # ← Add this line
    fee.save()

    return redirect("student_fees")