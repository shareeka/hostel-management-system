from django.urls import path
from . import views

urlpatterns = [

path('add-notice/', views.add_notice, name="add_notice"),
path('view-notices/', views.view_notice, name="view_notice"),
path('delete-notice/<int:id>/', views.delete_notice, name="delete_notice"),

]