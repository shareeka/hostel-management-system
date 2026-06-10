from django.urls import path
from . import views

urlpatterns = [

path('add-student/', views.add_student, name="add_student"),
path('view-students/', views.view_students, name="view_students"),
path('delete-student/<int:id>/', views.delete_student),
path('register/', views.student_register, name="student_register"),
path('login/', views.student_login, name="student_login"),
path('dashboard/', views.student_dashboard, name="student_dashboard"),
path('student_logout/', views.student_logout, name="student_logout"),
path('notices/', views.student_notices, name="student_notices"),
path('vacant-students/', views.vacant_students),
path('student-room/', views.student_room, name="student_room"),

]