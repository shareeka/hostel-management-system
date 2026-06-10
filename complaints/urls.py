from django.urls import path
from . import views

urlpatterns = [

path('add/', views.add_complaint, name="add_complaint"),
    path('view/', views.view_complaints, name="view_complaints"),
    path('resolve/<int:id>/', views.resolve_complaint, name="resolve_complaint"),

]