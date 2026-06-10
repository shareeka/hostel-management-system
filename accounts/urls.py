from django.urls import path
from . import views

urlpatterns = [

path('', views.home),
path('admin-login/', views.admin_login, name="admin_login"),
path('admin-logout/', views.admin_logout, name='admin_logout'),
path('dashboard/', views.admin_dashboard, name="admin_dashboard"),

path('warden-login/', views.warden_login, name="warden_login"),
path('warden-dashboard/', views.warden_dashboard, name="warden_dashboard"),
path('warden-logout/', views.warden_logout, name="warden_logout"),

path('add-warden/', views.add_warden, name="add_warden"),
path('view-wardens/', views.view_wardens, name="view_wardens"),
path('delete-warden/<int:id>/', views.delete_warden),

]