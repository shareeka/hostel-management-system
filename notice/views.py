from django.shortcuts import render, redirect
from .models import Notice


def add_notice(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")

        Notice.objects.create(
            title=title,
            description=description
        )

        return redirect("view_notice")

    return render(request,"add_notice.html")



def view_notice(request):

    notices = Notice.objects.all().order_by("-id")

    return render(request,"view_notice.html",{"notices":notices})



def delete_notice(request,id):

    notice = Notice.objects.get(id=id)
    notice.delete()

    return redirect("view_notice")