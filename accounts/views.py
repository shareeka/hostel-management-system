from django.shortcuts import render, redirect
from students.models import Student
from rooms.models import Room
from fees.models import Fee
from complaints.models import Complaint
def home(request):
    return render(request,"home.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin":
            # store session
            request.session['admin_logged_in'] = True
            return redirect("admin_dashboard")

    return render(request, "admin_login.html")

def admin_logout(request):
    # remove admin session
    if 'admin_logged_in' in request.session:
        del request.session['admin_logged_in']
    return redirect("admin_login")



def admin_dashboard(request):

    students = Student.objects.count()
    rooms = Room.objects.count()
    fees = Fee.objects.filter(status="Pending").count()
    complaints = Complaint.objects.count()

    context = {
        "students":students,
        "rooms":rooms,
        "fees":fees,
        "complaints":complaints
    }

    return render(request, "admin_dashboard.html", context)

from students.models import Student
from rooms.models import Room
from complaints.models import Complaint
from .models import Warden

def warden_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            warden = Warden.objects.get(
                username=username,
                password=password
            )

            request.session['warden_id'] = warden.id

            return redirect("warden_dashboard")

        except:
            pass

    return render(request,"warden_login.html")
  
def warden_dashboard(request):

    warden_id = request.session.get('warden_id')

    warden = Warden.objects.get(id=warden_id)

    students = Student.objects.count()
    rooms = Room.objects.count()
    complaints = Complaint.objects.count()

    context = {
        "warden":warden,
        "students":students,
        "rooms":rooms,
        "complaints":complaints
    }

    return render(request,"warden_dashboard.html",context)

def warden_logout(request):

    del request.session['warden_id']

    return redirect("warden_login")

def add_warden(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        username = request.POST.get("username")
        password = request.POST.get("password")

        photo = request.FILES.get("photo")

        Warden.objects.create(
            name=name,
            email=email,
            phone=phone,
            username=username,
            password=password,
            photo=photo
        )

        return redirect("view_wardens")

    return render(request,"add_warden.html")
  
def view_wardens(request):

    wardens = Warden.objects.all()

    return render(request,"view_wardens.html",{"wardens":wardens})
  
def delete_warden(request,id):

    warden = Warden.objects.get(id=id)
    warden.delete()

    return redirect("view_wardens")


# View all complaints (admin/warden)
def view_complaints(request):
    complaints = Complaint.objects.all().order_by('-date')
    return render(request, "view_complaints.html", {"complaints": complaints})

# Mark complaint as resolved
def resolve_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.status = "Resolved"
    complaint.save()
    return redirect("view_complaints")