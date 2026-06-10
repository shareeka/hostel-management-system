from django.urls import path
from . import views

urlpatterns = [

path('add-fee/', views.add_fee, name="add_fee"),
path('view-fees/', views.view_fees, name="view_fees"),
path('mark-paid/<int:id>/', views.mark_paid),
path('student-fees/', views.student_fees, name="student_fees"),
path('pay/<int:id>/', views.pay_fee, name="pay_fee"),

]